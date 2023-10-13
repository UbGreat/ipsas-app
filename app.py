from flask import Flask, render_template

TRANSACTIONS = [
    {
        "id": 1,
        "type": "expense",
        "name": "Payment for Malaria Treatment",
        "amount": -50000,
        "date": "2023-03-01",
        "purpose": "Primary Healthcare",
        "location": "Ikot Esenam"
    },
    {
        "id": 2,
        "type": "revenue",
        "name": "Internal Revenue",
        "amount": +120000,
        "date": "2023-03-02",
        "purpose": "Uyo capital tax",
        "location": "Uyo"
    },
    {
        "id": 3,
        "type": "expense",
        "name": "Transportation",
        "amount": -20000,
        "date": "2023-03-05",
        "purpose": "Visit to Aso Rock",
        "location": "Uyo"
    },
]

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/login")
def login():
  return render_template("login.html")


@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html", transactions=TRANSACTIONS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
