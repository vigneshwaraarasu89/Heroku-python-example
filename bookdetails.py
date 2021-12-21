# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:08:17 2021

@author: Admin
"""

from flask import Flask
app = Flask(__name__)
 
@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
 
if __name__ == '__main__':
   app.run()