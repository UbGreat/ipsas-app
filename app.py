from flask import Flask, render_template, jsonify

TRANSACTIONS = [
    {
        "id": 1,
        "type": "expense",
        "name": "Payment for Malaria Treatment",
        "amount": -50000,
        "date": "2023-03-04",
        "purpose": "Primary Healthcare",
        "location": "Ikot Esenam"
    },
    {
        "id": 2,
        "type": "revenue",
        "name": "Internal Revenue",
        "amount": +120000,
        "date": "2023-03-01",
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
  return render_template("index.html", page='Home')


@app.route("/login")
def login():
  return render_template("login.html", page='Login')


@app.route("/dashboard")
def dashboard():
  return render_template("dashboard.html",
                         transactions=TRANSACTIONS,
                         page='Dashboard')


# api routes
@app.route("/api/transactions")
def list_transactions():
  return jsonify(TRANSACTIONS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
