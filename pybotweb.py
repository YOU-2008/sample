from bottle import route, run, template, request
from datetime import datetime
import sys
sys.path.append("/Macintosh HD/ユーザ/you/Python/Python2nd/pybot3")
from pybot3 import pybot

@route("/hello")
def hello():
    now = datetime.now()
    return template("pybot_template.html", text="")

@route("/hello",method="POST")
def do_hello():
    #フォームから受け取ったテキストをinput_text
    input_text = request.forms.get("input_text")
    #input_textを引数にpybot関数を実行してresponseをoutput_textに代入
    output_text = pybot(input_text)
    #input_text,output_textをtemplateに渡す
    
    return template("pybot_template.html", text=input_text)
    input_text=request.forms.input_text
    return template("pybot_template.html",text=input_text)
    
    #return template("pybot_template.html", text=input_text, response=output_text)

run(host= "localhost" , post= 8080, debug= True)