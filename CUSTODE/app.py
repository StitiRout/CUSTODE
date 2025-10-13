from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/basics", methods=["GET", "POST"])
def basics():
    result = None
    if request.method == "POST":
        answer = request.form.get("gear")
        if answer == "Neutral":
            result = "✅ Correct! Always start the car in Neutral."
        else:
            result = "❌ Incorrect. The correct answer is Neutral."
    return render_template("basics.html", result=result)

@app.route("/safety", methods=["GET", "POST"])
def safety():
    result = None
    if request.method == "POST":
        answer = request.form.get("rule")
        if answer == "Seatbelt":
            result = "✅ Correct! Seatbelt is the most basic safety rule."
        else:
            result = "❌ Incorrect. You must always wear a seatbelt."
    return render_template("safety.html", result=result)

@app.route("/intrusion", methods=["GET"])
def intrusion():
    return render_template("intrusion.html")

if __name__ == "__main__":
    app.run(debug=True)
