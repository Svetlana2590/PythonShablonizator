from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            number = float(request.form["number"])
            result = number + 4
            print(f"Результат: {result}")
        except ValueError:
            error = "Введите число"

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)