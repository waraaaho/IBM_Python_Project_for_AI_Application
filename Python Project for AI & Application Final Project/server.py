from flask import Flask, render_template,request
import json

app = Flask("First Translate Server")
#books = []

from machinetranslation import translator


@app.route("/englishToSpanish")
def englishToSpanish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(textToTranslate)['translations'][0]['translation']

@app.route("/spanishToEnglish")
def spanishToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(textToTranslate)['translations'][0]['translation']
@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
