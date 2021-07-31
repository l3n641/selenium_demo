from flask import Flask
from flask.cli import load_dotenv
from flask import request
import os

app = Flask(__name__)

load_dotenv()


@app.route("/cookie", methods=['POST'])
def cookie():
    if request.form.get("cookie"):
        cookie_dir = os.getenv("COOKIE_DIR")
        cookie_file_name = os.getenv("COOKIE_FILE_NAME")
        if not os.path.exists(cookie_dir):
            os.makedirs(cookie_dir)
        file_path = os.path.join(cookie_dir, cookie_file_name)
        with open(file_path, "w") as f:
            f.write(request.form.get("cookie").strip())
        return 'ok', 200
    return "", 400
