import json

from selenium.webdriver.chrome.options import Options
from seleniumwrapper import create

options = Options()
options.add_argument('--headless')

browser = create('chrome', chrome_options=options)
QUESTIONS = []
try:
    browser.get('https://jeopardyanswers.org/jeopardy-world-tour-answers/')
    li_list = browser.xpath("//ul[@id='lcp_instance_0']//li", eager=True)
    question_urls = []
    for li in li_list:
        url = li.xpath('.//a').get_attribute('href')
        question_urls.append(url)
    for url in question_urls:
        browser.get(url)
        question = browser.xpath("//div[@class='question']").text
        question = question.replace('QUESTION: ', '')
        answer = browser.xpath("//div[@class='answer']").text
        answer = answer.replace('ANSWER: ', '')
        QUESTIONS.append({
            'question': question,
            'answer': answer
        })
        print('LEN: {}'.format(len(QUESTIONS)))
    with open('questions.json', 'w') as f:
        f.write(json.dumps(QUESTIONS))
    print('Done')
finally:
    browser.quit()
