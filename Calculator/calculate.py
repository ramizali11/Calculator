from flask import Flask, request, render_template
from simpleeval import simple_eval as sum

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calc():
    display = request.form.get("display", " ")

    if request.method == "POST":
      reuse = None
      if "key" in request.form:
        value = request.form["key"]
        display =request.form.get("display", " ") + value
        reuse = display

      elif "equal" in request.form:
        try:
          display = sum(request.form.get("display", " "))
        except:
          display = ""

      elif "clear" in request.form:
        display = " "

      elif "reverce" in request.form:
         display = request.form.get("display", "")
         display = display[:-1]

      elif "game" in request.form:
        step = request.form.get("step", "0")
    
  
    return render_template("index.html", display=display)

if __name__ == "__main__":
    app.run(debug=True)
