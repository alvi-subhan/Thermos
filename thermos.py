from flask import Flask, render_template, \
url_for

app = Flask(__name__)


class User():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return self.firstname


@app.route("/")
@app.route("/index  ")
def index():
    return render_template('index.html',title=5+4,user=User("subhan","alvi"))

"""@app.route("/aboutUs")
def about():
    return render_template('about.html')"""


#(it works without this command)
#if __name__=="__main__":
app.run(debug=True)
