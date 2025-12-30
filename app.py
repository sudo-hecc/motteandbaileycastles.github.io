from flask import Flask, redirect, url_for

# INITIALISE WEB APPLICATION (use default `static/` folder)
app = Flask(__name__)


# DEFINE ROUTES
@app.route("/")
def index():
    # Redirect to the static HTML so its CSS is loaded directly
    return redirect(url_for('static', filename='pages/main_page.html'))

# RUN WEB APPLICATION
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)