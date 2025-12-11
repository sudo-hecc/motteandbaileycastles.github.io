from flask import Flask, render_template_string
import logging
import os

# INITIALISE WEB APPLICATION
app = Flask(__name__)

# SETUP HTML TEMPLATE
HERE = os.path.dirname("pages/")

with open(os.path.join(HERE, "main_page.html"), "r") as f:
    TEMPLATE = f.read()

# DEFINE ROUTES
@app.route("/")
def index():
    return render_template_string(TEMPLATE)

# RUN WEB APPLICATION
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Waitress on 0.0.0.0:10000")
    print("Starting Waitress on 0.0.0.0:10000")
    try:
        from waitress import serve
        serve(app, host="0.0.0.0", port=10000)
    except Exception:
        logging.exception("Failed to start Waitress")
        raise