from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    current_y = datetime.datetime.now().year
    return render_template( 'index.html', c_year=current_y)


if __name__ == '__main__':
    app.run()
