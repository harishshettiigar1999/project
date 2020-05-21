# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:17:33 2020

@author: HARISH
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#import temp

#import model

app = Flask(__name__)
@app.route('/')
def classify():
   return render_template('index1.html')
'''
@app.route('/summarize', methods=['POST'])
def summarize():
    response = None
    if request.method == 'POST' :
        try:
            req_data = request.get_json()
            #print req_data
            #print req_data['top_sentences']
            response = summarization.summarize(req_data['data'],int(req_data['top_sentences']))
        except Exception as e:
            return respond(e)
       
    return respond(None, res=response)


def respond(err, res=None):
    return_res =  {
        'status_code': 400 if err else 200,
        'body': err.message if err else res,
    }
    return jsonify(return_res)
'''
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)