from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

#responses = []

@app.get("/")
def home_page():
    """ Shows survey start page with survey title, survey instructions,
    and start button """
    #responses.clear()
    session["responses"] = []

    return render_template('survey_start.html', survey = survey)


@app.post("/begin")
def begin():
    """redirects to questions route"""
    return redirect("/questions/0")


@app.get("/questions/<int:id>")
def question(id):
    """ populates question page"""

    if len(session["responses"]) == len(survey.questions):
        return redirect("/thank_you")

    if id > len(session["responses"]):
        return redirect(f'/questions/{len(session["responses"])}')

    """survey_question = survey.questions[id].question
    survey_choices = survey.questions[id].choices"""

    return render_template('question.html',
                            survey_question = survey.questions[id].question,
                            survey_choices = survey.questions[id].choices)


@app.post("/answer")
def add_answer():
    """adds answers to responses list variable"""
    #responses.append(request.form['answer'])
    responses = session["responses"]
    responses.append(request.form['answer'])
    session["responses"] = responses

    if len(responses) == len(survey.questions):
        return redirect("/thank_you")

    return redirect(f'/questions/{len(responses)}')


@app.get('/thank_you')
def thank_you():
    """ route to thank you page"""
    return render_template('completion.html')
