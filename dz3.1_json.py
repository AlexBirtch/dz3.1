from pprint import pprint
import json

# with open("newsafr.json", encoding="utf-8") as f:
#     json_data = json.load(f)
# print(json_data)
#
# with open("newsafr1.json", "w", encoding="utf-8") as f:
#     json.dump(json_data, f, ensure_ascii=False, indent=2)


file_name = 'newsafr.json'

def find_six_and_more(f_name):
    """
            находим слова длиннее 6-ти символов

    """

    six_more_lst = []

    for news in f_name['rss']['channel']['items']:
        description = news['description']

        for i in description.split():
            if len(i) > 6:
                six_more_lst.append(i.lower())

    return six_more_lst



def return_top_ten(list):
    """
            возвращаем топ 10 слов
    """

    word = ''
    lst = []

    for i in range (10):
        max = 0

        for i in list:
            count = list.count(i)
            if count > max and i not in lst:
                max = count
                word = i

        lst.append(word)
        print(f'{word}   :   встречается {max} раз')


with open(file_name, encoding='utf-8') as f:
    file = json.load(f)
    six_more_list = find_six_and_more(file)
    return_top_ten(six_more_list)
