import random

from flask import request, render_template, Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    roast = None
    if request.method == "POST":
        username = request.form.get("username")
        roasts = [
            f"{username}? wtf?",
            f"{username}? 0/10 ",
            f"{username}? Bruh..",
            f"{username}? That's ugly af bruh...",
        ]
        roast = random.choice(roasts)  # pick one roast randomly
    
    return render_template("sample.html", roast=roast)

if __name__ == "__main__":
    app.run(debug=True)
