def Read_dictionary():
    '''Чтение словаря'''
    try:
        input_dict = open('resulting.txt', 'r')
        raw_dictionary = input_dict.readlines()
        input_dict.close()
    except FileNotFoundError:
        print("Словарь не найден")
    dict_id = []
    dict_popularity = []
    dict_word = []
    dict_part = []
    for line in raw_dictionary:
        s = list(map(str, line.split()))
        dict_id.append(s[0])
        dict_popularity.append(s[1])
        dict_word.append(s[2])
        dict_part.append(s[3])
    print("Словарь усепшно подключен")
    # Вывод словаря
    # for i in dict_id:
    #     print("ID: {}, POPULARITY: {}, WORD: {}, PART: {}".format(dict_id[int(i) - 1],
    #                                                               dict_popularity[int(i) - 1], dict_word[int(i) - 1],
    #                                                               dict_part[int(i) - 1]))
    return dict_id, dict_popularity, dict_word, dict_part


def Read_input():
    '''Чтение файла ввода'''
    text = []
    inp_word = open('input.txt', 'r')
    words = inp_word.readlines()
    inp_word.close()
    for l in words:
        s = list(map(str, l.split()))
        x = 0
        for j in range(len(s)):
            text.append(s[x].lower())
            x += 1
    print("Input word:", end='')
    for element in range(len(text)):
        print(" {}".format(text[element]), end='')
    print("")
    return text


def Smart_change(word=""):
    '''Преобразует слово \n
    возвращает результат преобразований'''
    for i in range(len(word)):
        try:
            if word[i] == 'ё':
                word = word[:i] + 'е' + word[i + 1:]
            elif word[i] == '.' or word[i] == ',':
                word = word[:i]
        except IndexError:
            break
    # print(word, end='')
    return word


def Search(word="", dict_id=-1, dict_word=""):
    '''Алгоритм поиска \n
     Возвращает id слова из словаря'''
    max_count = 0
    max_id = 0
    for j in dict_id:
        count = 0
        for i in range(len(word)):
            try:
                if word[i] == str(dict_word[int(j)])[i]:
                    if str(word) == str(dict_word[int(j)]):
                        return dict_id[int(j)]
                    count += 1
                else:
                    if count > max_count:
                        max_count = count
                        max_id = int(j)
                    count = 0
            except IndexError:
                break
    return dict_id[max_id]


def Print_matrix(word="", dict_word=""):
    '''Выводит на экран матирицу'''
    print("\n", end="  ")
    for l in word:
        print(l, end=" ")
    print("")
    x = ""
    for i in range(len(dict_word)):
        for j in range(len(word)):
            try:
                if dict_word[i] == word[j]:
                    x += "X "
                else:
                    x += "o "
            except IndexError:
                print("0x00000001")
                break
        x += str(i)
        print(dict_word[i] + " " + x)
        x = ""
    print(end="  ")
    for l in range(len(word)):
        print(l, end=" ")


(dict_id, dict_popularity, dict_word, dict_part) = Read_dictionary()
text = Read_input()
for element in range(len(text)):
    word = Smart_change(text[element])
    word_id = Search(word, dict_id, dict_word)
    print("<" + str(word_id), end=' ')
    print(dict_word[int(word_id)] + ">", end='')
print()
