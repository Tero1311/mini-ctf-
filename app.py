from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/challenge1")
def challenge1():
    return render_template("challenge1.html") 

@app.route("/challenge2")
def challenge2():
    return render_template("challenge2.html")

@app.route("/challenge3")
def challenge3():
    return render_template("challenge3.html")


  
@app.route("/submit/challenge1", methods=["POST"])
def submit_challenge1():

    flag = request.form.get("flag")

    if flag == "FLAG{source_code_is_information}":
        return """
        <h1>🎉 Correct!</h1>
        <p>Challenge 1 completed!</p>
        <a href="/">Back to CTF</a>
        """

    return """
    <h1>❌ Incorrect!</h1>
    <p>That's not the correct flag.</p>
    <a href="/challenge1">Try Again</a>
    """
@app.route("/secret")
def secret():
    return render_template("secret.html")

@app.route("/submit/challenge2", methods=["POST"])
def submit_challenge2():

    flag = request.form.get("flag")

    if flag == "FLAG{hidden_endpoints_can_be_found}":
        return """
        <h1>🎉 Correct!</h1>
        <p>Challenge 2 completed!</p>
        <a href="/">Back to CTF</a>
        """

    return """
    <h1>❌ Incorrect!</h1>
    <p>That's not the correct flag.</p>
    <a href="/secret">Try Again</a>
    """


@app.route("/submit/challenge3", methods=["POST"])
def submit_challenge3():

    flag = request.form.get("flag")

    if flag == "FLAG{client_side_is_not_secret}":
        return """
        <h1>🎉 Correct!</h1>
        <p>Challenge 3 completed!</p>
        <a href="/">Back to CTF</a>
        """

    return """
    <h1>❌ Incorrect!</h1>
    <p>That's not the correct flag.</p>
    <a href="/challenge3">Try Again</a>
    """

if __name__ == "__main__":
    app.run(debug=True)