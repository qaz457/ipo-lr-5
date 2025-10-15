#Andrey
score = 1#создаем счетчик
print('Программа переносит информацию с одного файла в другой')#рассказываем что делает программа

with open('text.txt', 'r', encoding='utf-8') as file:#открываем файл для чтения
    lines = file.readlines()#записваем каждую строку в массив

with open('output.txt', 'w', encoding='utf-8') as file_2:#открывыаем новый файл для записи
    for line in lines:#проходимся по массиву
        file_2.write(f'{score}:{line.strip()}\n')#записваем каждую строчку прошлого файла  в новый 
        score += 1#добавляем 1 в счетчик
