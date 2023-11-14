from flask import Flask, request, jsonify, render_template, redirect
import json 
import main
#import backend

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return render_template('index.html')

@app.route("/text", methods = ['GET'])
def text_handling():
    return render_template('text.html')

# Use PHP for file handling
@app.route("/files", methods = ['GET'])
def files_handling():
    return render_template('file.html')

@app.route('/process', methods = ['POST'])
def process():
    data = request.get_json()
    text =data['text']
    dest_lang_code = data['dest_lang_code']
    src_lang = data['src_lang_code']
    response = main.main_translation(text,dest_lang_code, src_lang)
    out_file = open("sample.json", "w") 
    json.dump(response, out_file)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)