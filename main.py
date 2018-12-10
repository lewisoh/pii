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
    
    
    

    doc = nlp(sentence)    
    sentence = doc.text

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            sentence = re.sub(ent.text, '**PII-NAME**', sentence)
        if ent.label_ == 'ORG':
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
