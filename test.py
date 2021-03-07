import re

result = re.match(r'AV', 'AV match') # Искомая подстрока найдена. Чтобы вывести её содержимое, применим метод group() (мы используем «r» перед строкой шаблона, чтобы показать, что это «сырая» строка в Python):
print(result.group(0))

result = re.search(r'match', 'AV match')
print(result.group(0))

alls = []
list_1 = ('hello hello hello hello hello hello hello hello hello world bitch syka syka naxyu blyatsuka blyeat')
for i in list_1.split(' '):
    if i not in alls:
        result = re.findall(i, list_1)
        print(i, ' count ', len(result))
        alls.append(i)


#re.sub(pattern, repl, string)
#Ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не найден, строка остается неизменной.

result = re.sub(r'India', 'the World', 'AV is largest Analytics community of India') # re.sub работает как replace
print(result)

#Результат:
#'AV is largest Analytics community of the World'



#re.compile(pattern, repl, string)
#Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска. Это также избавляет от переписывания одного и того же выражения.

pattern = re.compile('AV')
result = pattern.findall('AV Analytics Vidhya AV')
print(result)
result2 = pattern.findall('AV is largest analytics community of India')
print(result2)

#Результат:
#['AV', 'AV']
#['AV']

test = str(input('test > '))
"""
Оператор	Описание
.	Один любой символ, кроме новой строки \n.
?	0 или 1 вхождение шаблона слева
+	1 и более вхождений шаблона слева
*	0 и более вхождений шаблона слева
\w	Любая цифра или буква (\W — все, кроме буквы или цифры)
\d	Любая цифра [0-9] (\D — все, кроме цифры)
\s	Любой пробельный символ (\S — любой непробельный символ)
\b	Граница слова
[..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
\	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
^ и $	Начало и конец строки соответственно
{n,m}	От n до m вхождений ({,m} — от 0 до m)
a|b	Соответствует a или b
()	Группирует выражение и возвращает найденный текст
\t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно

"""
result = re.sub(r'[\s\t\n\r]', '', test)
res = re.findall(r'[\+\-\/\*]', result)
print(res)
print(result)
print(eval(result))





text = str(input())
result = re.findall(r'(\w+)@', text)
print(result)
print(re.findall(r'@[A-Za-z\.]+', text))
