import json

from flask import Flask, render_template
from imap_tools import MailBox
from settings import EMAIL, PASSWORD, EMAIL_URL

app = Flask(__name__)


@app.route('/')
def index():
    data = None
    with MailBox(EMAIL_URL).login(EMAIL, PASSWORD, 'inbox') as mailbox:
        for msg in mailbox.fetch(limit=1, reverse=True):
            data = json.loads(msg.text.strip())

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
