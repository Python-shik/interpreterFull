import datetime
import os

from src.AI import prompts
from src import actions
from src.AI.BASE import Gen


# Подключаем api ключ
if "gemini_api_key" not in os.listdir("src/AI/"):
    with open("src/AI/gemini_api_key", "w", encoding="utf-8") as f:
        f.write(input("[Gemini API Key] "))

# Инициализируем AI
ai = Gen()
ai.system_instructions = [
    {"text": prompts.Instructions.first_instruction},
    {"text": prompts.Instructions.action_instruction},
    {"text": prompts.Instructions.examples}]
ai.import_history_anyway("conversations/history")


msg = None

while True:
    if not msg:
        msg = f"{str(datetime.datetime.now())}\nfrom_user||"+input("[user] ")
    ai.history_add("user", msg)
    result = ai.generate()
    ai.history_add("assistant", result)
    try:
        target = result.split("||")[0]

        # Если сообщение адресовано пользователю
        if target.lower() == "user":
            print("[assistant] " + result.split("||")[1])
            ai.export_history("conversations/history")
            msg = None

        # Если сообщение адресовано системе
        elif target.lower() == "system":
            splitted_result = result.split("||")
            title = splitted_result[1]
            print("[assistant] ", title)
            code_lang = splitted_result[2]
            if code_lang == "python":
                func4exec = splitted_result[3]
                """Представим, что ИИ ответил нам в следующем формате:

def f4exec():
    import datetime

    return str({"time": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")})
    
От нас теперь требуется:
1. Запустить эту функцию
2. Получить результат выполнения этой функции"""

                exec(func4exec)

                result = eval("f4exec()")

                msg = f"{str(datetime.datetime.now())}\n{result}"


    except Exception as e:
        print(e)
        msg = 'error||' + str(e)


