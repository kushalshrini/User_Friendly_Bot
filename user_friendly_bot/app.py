import warnings
from flask import Flask, render_template, request
from chatbot import chatbot


warnings.filterwarnings('ignore')
# download
app = Flask(__name__)

app.register_blueprint(chatbot, url_prefix="/c")

@app.route("/")
def home():

    return render_template("Login.html")


if __name__ == "__main__":
    app.run(debug=True)  # debug=True


