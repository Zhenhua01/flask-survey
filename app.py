from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get("/")
def home_page():
    """ Shows survey start page with survey title, survey instructions,
    and start button """

    survey_title = survey.title
    survey_instructions = survey.instructions

    return render_template('survey_start.html', survey_title = survey_title,
                            survey_instructions = survey_instructions)

@app.post("/begin")
def begin():
    return redirect("/questions/0")

@app.get("/questions/<int:id>")
def question(id):
    survey_question = survey.questions[id].question
    survey_choices = survey.questions[id].choices
    """ Grabs question """
    return render_template('question.html', survey_question = survey_question,
                            survey_choices = survey_choices)
