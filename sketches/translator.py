""" Переводв вопросов на русский
"""
import json
import time

from googletrans import Translator

translator = Translator()


with open('questions.json') as f:
    questions = json.loads(f.read())

new_questions = []
for question in questions:
    en_question = question['en_question'].strip()
    en_answer = question['en_answer'].strip()
    try:
        ru_question = translator.translate(en_question, src='en', dest='ru').text
        ru_answer = translator.translate(en_answer, src='en', dest='ru').text
    except Exception as e:
        ru_question = None
        ru_answer = None
        print(e)
    question['ru_question'] = ru_question
    question['ru_answer'] = ru_answer
    new_questions.append(question)

with open('all_questions.json', 'w') as f:
    f.write(json.dumps(new_questions))