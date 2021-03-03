"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template

app = Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
"""1. Add a View Function for the Home page."""
@app.route('/')
def hello():
    return render_template("paws_css_home.html")


@app.route('/about')
def about():
    return render_template("paws_css_about.html")


if __name__ == "__main__":
    """ """
    app.run(debug=True)