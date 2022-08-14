from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

global job_results
job_results = []


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        job = request.form.get('job')
        job_results.append(job)
        print(job_results)
        return render_template('index.html',job_results=job_results)
    else:
        return render_template('index.html')

    return render_template("index.html", job_results=job_results)


''''@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))'''

if __name__ == "__main__":
    app.run(debug=True)