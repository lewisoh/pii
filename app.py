from flask import Flask, redirect, url_for, request
import spacy
import re
import json

	
nlp = spacy.load('en_core_web_sm')
app = Flask(__name__)


        
@app.route("/", methods=['POST'])
def parse_text():

    input = request.get_json()
    print(input)
    sentence = json.dumps(input)
    
    
    sentence = re.sub(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b', '**PII-PC**', sentence)
    sentence = re.sub(r'\b4[0-9]{12}(?:[0-9]{3})?\b', '**PII-CC**', sentence)

    doc = nlp(sentence)    
    sentence = doc.text

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            sentence = re.sub(ent.text, '**PII-NAME**', sentence)
        if ent.label_ == 'NUM':
            sentence = re.sub(ent.text, '**PII-NUM**', sentence) 
        if ent.label_ == 'DATE':
            sentence = re.sub(ent.text, '**PII-NUM**', sentence)
        if ent.label_ == 'CARDINAL':
            sentence = re.sub(ent.text, '**PII-NUM**', sentence)
        print("test")
        print("sentence")

    


    #sentence = " ".join(sentence)

    return sentence
    

if __name__ == "__main__":
	app.run(host='0.0.0.0')