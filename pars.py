from pyparsing import Word, Literal, nums, alphas
import json

rus_alphas = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
rus_alphanums = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234567890,.:;()«»-–'  #Короткое (среднее) тире – Alt + 0150; Дефиc - клавиша на клавиатуре

f = open('destiny.txt', 'r')
lines = f.readlines()
text = ' '.join(lines)

text = text.replace("\r","")
text = text.replace("\n","")

Dash = Literal('—')  #тире (длинное)	—	Alt + 0151
Number = Word(nums) + Dash.suppress()
Name = Word(nums).suppress() + Dash.suppress() + Word(rus_alphanums)

#Шаблон для поиска описания
Description = Name.suppress() + Word(rus_alphanums + ' ') + Literal('/').suppress()

destinyData = {}

for num in Number.searchString(text):
    key = int(num[0])
    destinyData[key] = dict({'number' : num[0]})

key = 1
for name in Name.searchString(text):        
    destinyData[key].update({'name' : name[0]})
    key += 1

key = 1
for description in Description.searchString(text):
    destinyData[key].update({'description' : description[0]})
    key += 1

#print(json.dumps(densityData, ensure_ascii = False, sort_keys = True, indent = 4))

with open("json/destinyData.json", "w", encoding="utf-8") as file:
    json.dump(destinyData, file, ensure_ascii = False, sort_keys = True, indent = 4)

