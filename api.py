# livinus felix bassey
# vefforritun1
# 21.09.2018

from bottle import *
import json

# að Tengja við skránna gengi.json

@route('/')
def index():
    with open("gengi.json","r") as skra:
        uppli = json.load(skra)
    return template('index.tpl',uppli)

run(host='localhost',port='8080',debug=True)


