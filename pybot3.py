from pybot_weather import weather_command
from pybot_datetime import today_command, now_command, weekday_command
from pybot_heisei import heisei_command
from pybot_len import len_command
from eto_multiple_data import eto_command
from pybot_random import choice_command
from pybot_randoms import dice_command
command_file = open("pybot.txt",encoding = "utf-8")
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()
bot_dict = {}
for O in lines:
    word_list = O.split ("、")
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

def pybot(input_text):
    try:
        command = input("ZGTパクリbot>") 
        response = ""
        if "サイコロ" in command:
            response = dice_command(command)
        if "選ぶ" in command:
            response = choice_command(command)
        if "干支" in command:
            response = eto_command(command)
        if "長さ" in command:
            response = len_command(command)
        if "今日" in command:
            response = today_command()
        if "現在" in command:
            response = now_command()
        if "曜日" in command:
            response = weekday_command(command)
        if "天気" in command:
            response = weather_command()
        for YOU in bot_dict:
            if YOU in command:
                response = bot_dict[YOU]
                break
            if not command:
                response = "何ヲ言ッテルカ、ワカラナイ"
        if "平成" in command:
            response = heisei_command(command)
        print(response)
#        if "さようなら" in command:
#            break
    except Exception as e:
        print("予期セヌエラーガ発生シマシタ")
        print("※ 種類:", type(e))
        print("※ 内容:", e)