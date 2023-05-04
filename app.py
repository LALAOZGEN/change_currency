from flask import Flask,render_template,request
import requests

api_key = "rjf8q8lcat8l99rco50b268srl2b9el4ii5aucs5d8f0a6pn8j238"

url = "https://anyapi.io/api/v1/exchange/rates?apiKey=" + api_key

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")

        amount = request.form.get("amount")
        response = requests.get(url)
        app.logger.info(response)

        infos = response.json()
        

        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue/firstValue) * float(amount)

        currencyInfo = dict()

        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        app.logger.info(infos)
        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)