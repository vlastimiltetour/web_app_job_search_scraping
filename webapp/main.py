from flask import Flask, render_template, request, redirect, url_for
from job_scraper import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/scrape', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        job_search = request.form.get('job_search')
        fresh_data = scrape_data(job_search)

        return render_template('home.html', job_results=fresh_data)
    else:
        print('ERROR')

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)