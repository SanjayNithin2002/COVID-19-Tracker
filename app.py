from flask import Flask, render_template, request,  redirect
from COVID import get_values
app = Flask(__name__)
countryData = dict()
stateData = dict()
@app.route("/")
def basic_route():
    return redirect("/posts")


@app.route("/posts" , methods = ["GET","POST"])
def route2():
    global stateData, countryData
    countryData = get_values()
    if request.method == "POST":
        req = request.form["state"]
        regionData = countryData["regionData"]
        temp = dict()
        for region in regionData:
            if region["region"] == req:
                temp = dict(region)
        stateData = temp
        return redirect("/stateSearch")
        
    
    return render_template("homepage.html",data = countryData)


@app.route("/stateSearch", methods = ['GET','POST'])
def route3():
    if request.method == 'POST':
        req = request.form["back"]
        if req=="true":
            return redirect("/")
        
    return render_template("stateData.html", data = stateData)



if __name__=="__main__":
    app.run(debug=True)