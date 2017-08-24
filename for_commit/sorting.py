import sqlite3 as lite
import sys

"""
Тут происходит чтение списка слов из файла lemma.al
Потом Занесение данных в SQL таблицу test.db с последующей сортировкой по убыванию частоты слов
В конце выносим эту таблицу обратно в resulting.txt файл в отсортированном виде
"""
#предварительно надо удалить верхнюю строчку с мусором из файла lemma.al (если есть)
def sorting():
    lems = open("lemma.al",'r')
    lines = lems.read().split('\n') #запись слов в список
    lems.close()

# #Уменьшем индекс(лишнее)
#     ind = 1
#     i = 0
#     for line in lines:
#         try:
#             line = line.replace(str(ind),str(ind-1))
#             ind+=1
#             lines[i] = line
#             i+=1
#         except EOFError:
#             print("Что-то не так...\n")

#запись в SQL таблицу
    try:
        con = lite.connect('test.db')
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Words")
        cur.execute("CREATE TABLE Words(Id INT, Popularity INT, Words TEXT, Part TEXT)")
        for line in lines:
            id = line[0:(line.find(' '))]
            line = line[line.find(' ')+1:]
            Popularity = line[0:line.find(' ')]
            line = line[line.find(' ') + 1:]
            Words = line[0:line.find(' ')]
            line = line[line.find(' ') + 1:]
            Part = line[0:line.find(' ')]
            line = line[line.find(' ') + 1:]

            cur.execute(("INSERT INTO Words VALUES('{}',{},'{}','{}')").format(int(id),float(Popularity),Words,Part))
        con.commit()

    except lite.Error as e:
        if con:
            con.rollback()

        print("Error %s:" % e.args[0])
        sys.exit(1)

    finally:
        if con:
            con.close()

# чтение таблицы
    con = lite.connect('test.db')
    resulting = ''
    i = 0
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Words ORDER BY Popularity DESC")
    while True:
        row = cur.fetchone() #Метод fetcone() получает следующую строку
        if row == None:
            break
        resulting += str(i) + ' ' + str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[3] + "\n")
        i+=1

#Итоговое сохранение файла
    print(resulting)
    lems = open("resulting.txt", 'w')
    lems.write(str(resulting))
    lems.close()

sorting()
