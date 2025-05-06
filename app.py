from flask import Flask, render_template, request
from ai_helper import explain_math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = ""
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            correct = eval(expression)  # matematik işlemini çözer
            feedback = f"✅ Cevap doğru: {correct}"
        except:
            feedback = "❌ Geçersiz işlem"

        explanation = explain_math(expression)
        return render_template("index.html", feedback=feedback, explanation=explanation)

    return render_template("index.html", feedback=None)

if __name__ == "__main__":
    app.run(debug=True)
