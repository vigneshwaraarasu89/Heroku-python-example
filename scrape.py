# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:08:17 2021

@author: Admin
"""
import requests
from flask import request
from flask import Flask
import re
import lxml
from lxml.html.clean import Cleaner
from lxml.html import document_fromstring
from datetime import datetime

app = Flask(__name__)
cleaner = Cleaner()
cleaner.javascript = True 
cleaner.style = True 
cleaner.comments = True
cleaner.style = True


@app.route('/')
def url_scrape():
    response={}
    url = request.args.get('url')
    page = requests.get(url)
    content = page.text
    doc = document_fromstring(content)
    content = lxml.html.tostring(cleaner.clean_html(doc))
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(content))
    cleantags = re.compile('&.*?;')
    cleantexts = re.sub(cleantags, '', cleantext)
    _RE_COMBINE_WHITESPACE = re.compile(r"(?a:\s+)")
    parsetext = re.sub(_RE_COMBINE_WHITESPACE, ' ', cleantexts)
    parsetext = parsetext.replace("\n", "")
    parsetext = parsetext.replace("\r", "")
    parsetext = parsetext.replace("\\'", "'")
    parsetext = parsetext.replace("\\n", "")
    parsetext = parsetext.replace("\\t", "")
    response['url']=url
    response['url_content']=parsetext
    response['url_content_timestamp']=datetime.now().utcnow()
    return response

app.run(debug = False)