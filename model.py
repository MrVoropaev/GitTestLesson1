spravka = 'phone_book.txt'

def read_phonebook():
    with open(spravka, 'r', encoding='utf8') as book:
        for line in book:
            return line.replace("\r", "").replace("\n", "")

def add_contact(contact):
    contact = input('Введите ФИО и телефон')
    with open(spravka, 'a', encoding='utf8') as book:
        book.write('\n' + contact)
    return 'Контакт успешно добавлен в справочник!'

def find(contact):
    with open(spravka, 'r', encoding='utf8') as book:
        count = 0
        for line in book:
            if contact in line:
                count = +1
                return(line.replace("\r", "").replace("\n", ""))
        if count == 0:
            return 'Нет данных, удовлетворяющих введенным значениям!'
