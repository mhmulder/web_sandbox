from flask import Flask, request, render_template
import pickle
from build_model import TextClassifier, get_data
app = Flask(__name__)


css_script='''<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script>window.jQuery || document.write('<script src="../statuc/js/jquery.min.js"><\/script>')</script>
<script src="../static/js/bootstrap.min.js"></script>
<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="../static/js/ie10-viewport-bug-workaround.js"></script>'''

@app.route('/')
def index():
    # display_str = '<h1>Welcome!</h1>'
    # # code below makes a button to go to the '/submit block
    # go_to_submit_html = '''
    #     <form action="/submit" >
    #         <input type="submit" value = "Go to submit"/>
    #     </form>
    # '''
    # # html that gets returned
    # return display_str + go_to_submit_html + css_script
    return render_template('index.html')

@app.route('/submit')
def submit_func():
    return render_template('submit.html')

# @app.route('/predict_jquery', methods = ["GET", "POST"])
# def predict_func2():
#     header = '<h1>Check out this awesome predict page page!</h1>'
#     # code below makes a button to go to the '/rainbow' block
#
#     insert_jq ='''<script
#       src="https://code.jquery.com/jquery-3.2.1.js"
#       integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE="
#       crossorigin="anonymous"></script>'''
#
#     with open('static/model.pkl', 'rb') as f:
#        model = pickle.load(f)
#
#     X = [request.form['words']]
#
#     prediction = model.predict(X)[0]
#
#     go_to_submit_html = '''
#         <br><br>
#         <form action="/submit" >
#             <input type="submit" value = "Submit Again?"/>
#         </form>
#     '''
#
#     go_home = '''
#         <form action="/" >
#             <input type="submit" value = "Go home"/>
#         </form>
#     '''
#     # html that gets returned
#     return header + prediction + go_to_submit_html + go_home

@app.route('/predict', methods = ["GET", "POST"])
def predict_func():
    header = '<h1>Check out this awesome predict page page!</h1>'
    # code below makes a button to go to the '/rainbow' block

    with open('static/model.pkl', 'rb') as f:
       model = pickle.load(f)

    X = [request.form['words']]

    prediction = model.predict(X)[0]

    # go_to_submit_html = '''
    #     <br><br>
    #     <form action="/submit" >
    #         <input type="submit" value = "Submit Again?"/>
    #     </form>
    # '''
    #
    # go_home = '''
    #     <form action="/" >
    #         <input type="submit" value = "Go home"/>
    #     </form>
    # '''
    # # html that gets returned
    # return header + prediction + go_to_submit_html + go_home + css_script
    return render_template('predict.html', prediction = prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
