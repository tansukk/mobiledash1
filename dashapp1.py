



from flask import Flask, render_template, flash, request, url_for, redirect, send_file

app = Flask(__name__)




@app.route('/')
@app.route('/dash1')
def dash1():

    return render_template("dash1.html")



if __name__ == "__main__":
    app.run(debug=True)