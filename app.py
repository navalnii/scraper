#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response, request, redirect, url_for
import pandas as pd 
import diff_time
from pandas import DataFrame

app = Flask(__name__)

@app.route('/')
def index():
    df = diff_time.list_emp('','','')
    
    return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/filter_data/', methods=['GET','POST'])
def filter_data():       
    if request.method == "POST":
        user = request.form['user']
        date_from = request.form['date_from']
        date_to = request.form['date_to']
        res = diff_time.list_emp(user, date_from, date_to)
        #print(user, date_from, date_to)
        return render_template('filter_data.html',  tables=[res.to_html(classes='data')], titles=res.columns.values)
        
    elif request.method == "GET":
        pass   
    
    return render_template('filter_data.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
