from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", title = "home") 

if __name__ == "__main__":
    app.run()