from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

# Sample username and password
USERNAME = "admin"
PASSWORD = "password"

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != USERNAME or request.form["password"] != PASSWORD:
            error = "Invalid credentials. Please try again."
        else:
            # Redirect to the home page after successful login
            return redirect(url_for("home"))
    return render_template("login.html", error=error)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/los")
def los():
    return render_template("los.html")

@app.route("/lms")
def lms():
    return render_template("lms.html")

@app.route("/collections")
def collections():
    return render_template("collections.html")

@app.route("/los/processing_summary")
def loan_processing_summary():
    return render_template("Loan_Processing_Summary.html")

@app.route("/los/processing_trend")
def loan_processing_trend():
    return render_template("Loan_Processing_Trend.html")

@app.route("/lms/portfolio_summary")
def portfolio_summary():
    return render_template("portfolio_summary.html")

@app.route("/lms/portfolio_performance")
def portfolio_performance():
    return render_template("portfolio_performance.html")

@app.route("/collections/debt_summary")
def debt_collection_summary():
    return render_template("debt_collection_summary.html")

@app.route("/collections/payment_trends")
def payment_trends():
    return render_template("payment_trends.html")

@app.route("/collections/performance")
def collection_performance():
    return render_template("collection_performance.html")

@app.route("/streamlit_app")
def streamlit_app():
    # Ensure Streamlit is running
    if 'streamlit_pid' not in globals():
        global streamlit_pid
        streamlit_pid = subprocess.Popen(['streamlit', 'run', 'streamlit_app.py']).pid
    
    # Render a page with the Streamlit app embedded
    return render_template("streamlit_app.html")

if __name__ == "__main__":
    app.run(debug=True)






