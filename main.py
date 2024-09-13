from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/say/") # like a directory without the end / it will works
def say():
    return "say" 

@app.route("/file") # like a file with a / at the  it will not work : because it's not a directory
def file():
    return "file content : papis"

# url avec extraction de parametres

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'valeur du post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {subpath}' 

# with request type
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "submit succes"
    else:
        return "submit the form"


@app.get('/login')
def login_get():
    return "login page"

@app.post('/login')
def login_post():
    return "login success"

if __name__ == '__main__':
    app.run(debug=True)



#flask --app main run --debug : live reload and error debug





#flask --app hello run