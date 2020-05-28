from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/welcome_to')
def welcome():
    return render_template('welcome_to.html')

@app.route('/main')
def main():
    return render_template('main.html')



if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)
