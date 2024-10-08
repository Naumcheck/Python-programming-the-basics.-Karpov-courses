'''

В базе данных МАИ информация о студентах и кафедрах, к которым они прикреплены, хранится в словаре kaf_students в формате: 
ключ — ФИ студента
значение — код кафедры. 

После второго курса по итогам последних двух сессий был составлен рейтинг студентов, на основе которого произошло перераспределение студентов по кафедрам.
Часть студентов продолжила обучение на своей кафедре, а некоторые студенты перешли с одной кафедры на другую. 
Информация о студентах, перешедших на новую кафедру, хранится в словаре new_kaf_students. 

Обновите информацию в словаре kaf_students, добавив в словарь данные из new_kaf_students.

Пример:

kaf_students  = {'Карпов Анатолий Дмитриевич': 100}
new_kaf_students =  {'Иванчей Иван Иванович': 200}

kaf_students = {'Карпов Анатолий Дмитриевич': 100, 'Иванчей Иван Иванович': 200}

'''
kaf_students.update(new_kaf_students)