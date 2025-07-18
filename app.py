from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return "<h2>Welcome! Visit /form-get or /form-post</h2>"

@app.route("/form-get")
def form_get():
    return render_template("form_get.html")

@app.route("/form-post")
def form_post():
    return render_template("form_post.html")

@app.route("/submit-get", methods=["GET"])
def submit_get():
    name = request.args.get("name")
    email = request.args.get("email")
    return f"<h3>GET Received:</h3><p>Name: {name}<br>Email: {email}</p>"

@app.route("/submit-post", methods=["POST"])
def submit_post():
    name = request.form["name"]
    course = request.form["course"]
    return f"<h3>POST Received:</h3><p>Name: {name}<br>Course: {course}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

