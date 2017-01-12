from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
     return render_template('index.html')


@app.route('/exploration_steps', methods=['GET', 'POST'])
def exploration_steps():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return 'Post was clicked'

    # show the form, it wasn't submitted
    return render_template('index2.html')


##Run Main Application
if __name__ == '__main__':
    app.debug = True
    app.run(port=33507)
