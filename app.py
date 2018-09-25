# livinus felix bassey
# vefforritun1
# 21.09.2018

from sys import argv
from bottle import *
import json

# að Tengja við skránna gengi.json

@route('/')
def index():
    with open("gengi.json","r") as skra:
        uppli = json.load(skra)
    return template('index.tpl',uppli)

run(host='0.0.0.0',port=argv[1] ,debug=True)


