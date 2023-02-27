# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя
def all_contacts():
    with open('phone_book.txt', 'r', encoding='utf-8')as data:
        for line in data:
            print(line)
        print()
def contact_search(name):
    res = []
    with open('phone_book.txt', 'r', encoding='utf-8')as data:
        for line in data:
            if name.title() in line:
                res.append(line)
        if len(res)>=1:
            print(*res, sep='\n')
        else: print('Контакт не найден')
        print()
def add_contact(n):
    res = []
    contact = ''
    with open('phone_book.txt', 'a', encoding='utf-8')as data:
        res.append(n.title())
        contact = ' '.join(res)
        data.write('\n'+contact)
        print('Контакт сохранён')
def delte_contact(w):
    name = str(w)
    with open("phone_book.txt", "r", encoding='utf-8') as data:
        contacts = data.readlines()
    with open("phone_book.txt","w", encoding='utf-8') as data:
        for i in contacts:
            if name in i:
                contacts.remove(i)
        data.writelines(contacts)

def change_contact(w):
    name = str(w)
    with open("phone_book.txt", "r", encoding='utf-8') as data:
        contacts = data.readlines()
    with open("phone_book.txt","w", encoding='utf-8') as data:
        for i in contacts:
            if name in i:
                c = i.split()
                c.remove(c[-1])
                c.append(input('Введите новый номер: '))
                contacts.remove(i)
                contacts.append('\n'+(' '.join(c)))
                break
        data.writelines(contacts)


while True:
    print()
    n = input('Введите "1"-показать контакты,"2"-для поиска контакта,"3"- добавить контакт,"4"- изменить контакт, 5-удалить и 6 - выйти из программы: ')
    print()
    if n == '1':
        print('Список контактов: ')
        all_contacts()
    elif n=='2':
        contact_search(input('Введите ФИО или номер: '))
    elif n== '3':
        add_contact(input('Введите ФИО и телефон нового контакта: '))
    elif n== '4':
        change_contact(input('Введите фамилию человека, чей номер вы хотите изменить: '))
    elif n=='5':
        delte_contact(input('Введите фамилию человека, чей номер вы хотите удалить: '))
    else:
        break



