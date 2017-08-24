import sqlite3 as lite
import sys
"""Тут создается SQL таблица с данными о словах:
База данных для слов с 3+ полями
Слово | Классификатор | Ассоциации (|) Возможные действия
"""

#запись в SQL таблицу
def mkSQL():
    """SQL табличка для тестового описания слов"""
    try:
        con = lite.connect('WordParams.db')
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Params")
        cur.execute("CREATE TABLE Params(Words TEXT, Class TEXT, Assoc TEXT, TODO TEXT)")

        cur.execute("INSERT INTO Params VALUES('Футболист','nou','мяч,футбол,игра','бегать,забивать')")
        cur.execute("INSERT INTO Params VALUES('бдеть','ver','смотреть,ожидать','ждать')")

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
    con = lite.connect('WordParams.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Params")
    while True:
        row = cur.fetchone() #Метод fetcone() получает следующую строку
        if row == None:
            break
        print(row[0],row[1],row[2],row[3])
mkSQL()