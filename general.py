from flask import Flask, request, render_template_string, session, redirect

app = Flask(__name__)
app.secret_key = "quizsecret"

questions = [

{"question":"Researchers have published their findings yesterday.","options":["Correct","Incorrect"],"answer":"Incorrect"},
{"question":"Scientists discovered a new species of butterfly in the Amazon rainforest.","options":["Correct","Incorrect"],"answer":"Correct"},
{"question":"BREAKING NEWS!!! Miracle fruit cures all diseases instantly!!!","options":["Real News Style","Fake News Style"],"answer":"Fake News Style"},
{"question":"Researchers have been studying climate change for ten years.","options":["Correct","Incorrect"],"answer":"Correct"},
{"question":"A blog claims a magical herb guarantees perfect health.","options":["Real News Style","Fake News Style"],"answer":"Fake News Style"},
{"question":"Scientists discovered water on Mars in 2015.","options":["Correct","Incorrect"],"answer":"Correct"},
{"question":"Scientists have discovered water on Mars in 2015.","options":["Correct","Incorrect"],"answer":"Incorrect"},
{"question":"The professor explains the results yesterday.","options":["Correct","Incorrect"],"answer":"Incorrect"},
{"question":"Researchers will present their findings next month.","options":["Correct","Incorrect"],"answer":"Correct"},
{"question":"SHOCKING!!! This drink will make you live forever!!!","options":["Real News Style","Fake News Style"],"answer":"Fake News Style"},
{"question":"The Earth revolves around the Sun.","options":["Correct","Incorrect"],"answer":"Correct"},
{"question":"The sun rises in the west.","options":["Correct","Incorrect"],"answer":"Incorrect"},
{"question":"Water freezes at 0°C.","options":["Correct","Incorrect"],"answer":"Correct"},
{"question":"Humans can breathe in space without equipment.","options":["Correct","Incorrect"],"answer":"Incorrect"},
{"question":"Light travels faster than sound.","options":["Correct","Incorrect"],"answer":"Correct"},
{"question":"BREAKING!!! Chocolate cures all diseases overnight.","options":["Real News Style","Fake News Style"],"answer":"Fake News Style"},
{"question":"Scientists say drinking water is essential for health.","options":["Real News Style","Fake News Style"],"answer":"Real News Style"},
{"question":"Eating one apple daily guarantees you will live 150 years.","options":["Real News Style","Fake News Style"],"answer":"Fake News Style"},
{"question":"WHO releases report on global vaccination programs.","options":["Real News Style","Fake News Style"],"answer":"Real News Style"},
{"question":"Miracle diet pill melts 20kg fat in one week!!!","options":["Real News Style","Fake News Style"],"answer":"Fake News Style"}

]

intro_html = """
<html>
<head>
<title>Escape the Misinformation</title>
<style>
body{
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
font-family:Arial;
color:white;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
}
.card{
background:#1c1c1c;
padding:40px;
border-radius:20px;
width:600px;
text-align:center;
}
button{
padding:15px 35px;
font-size:18px;
border:none;
border-radius:30px;
background:#00e5ff;
cursor:pointer;
}
</style>
</head>
<body>

<div class="card">

<h1>Escape the Misinformation</h1>

<p>
In today's digital world, information spreads very quickly through social media,
news websites, and online platforms. However, not all information we encounter
is reliable. Some statements contain exaggerated claims, misleading headlines,
or grammatical clues that indicate misinformation.
</p>

<p>
This quiz challenges you to analyze different statements and identify whether
they are correct, incorrect, or resemble fake news. By carefully observing
language patterns, tone, and logic, you can improve your critical thinking
skills and learn how to recognize misinformation.
</p>

<p>
Answer the questions carefully and try to achieve the highest score!
</p>

<br>

<a href="/quiz"><button>Start Quiz</button></a>

</div>

</body>
</html>
"""

quiz_html = """
<html>
<head>
<title>Escape the Misinformation</title>

<style>

body{
background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);
font-family:Arial;
color:white;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
}

.card{
background:#1c1c1c;
padding:40px;
border-radius:20px;
width:520px;
text-align:center;
}

.option{
display:block;
padding:12px;
margin:10px;
border:2px solid #444;
border-radius:10px;
cursor:pointer;
}

.option:hover{
background:#00e5ff;
color:black;
}

button{
padding:12px 30px;
margin-top:20px;
border:none;
border-radius:30px;
background:#00e5ff;
font-size:16px;
cursor:pointer;
}

.score{
font-size:50px;
color:#00ff9d;
}

</style>

</head>
<body>

<div class="card">

{% if finished %}

<h1>Quiz Completed 🎉</h1>

<div class="score">{{score}} / {{total}}</div>

<a href="/restart"><button>Play Again</button></a>

{% else %}

<h2>Question {{current}} of {{total}}</h2>

<form method="post">

<p>{{question}}</p>

{% for opt in options %}

<label class="option">
<input type="radio" name="answer" value="{{opt}}" required>
{{opt}}
</label>

{% endfor %}

<button type="submit">Next</button>

</form>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/")
def intro():
    return render_template_string(intro_html)

@app.route("/quiz", methods=["GET","POST"])
def quiz():

    if "index" not in session:
        session["index"]=0
        session["score"]=0

    if request.method=="POST":

        user_answer=request.form["answer"]
        correct=questions[session["index"]]["answer"]

        if user_answer==correct:
            session["score"]+=1

        session["index"]+=1

    if session["index"]>=len(questions):

        return render_template_string(
            quiz_html,
            finished=True,
            score=session["score"],
            total=len(questions)
        )

    q=questions[session["index"]]

    return render_template_string(
        quiz_html,
        finished=False,
        question=q["question"],
        options=q["options"],
        current=session["index"]+1,
        total=len(questions)
    )

@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)