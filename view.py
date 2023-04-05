def greetings():
    print('Приветствую! Выберите пункт, который вас интересует.')

def menu():
    print(""" Телефонный справочник

    1. Показать все контакты
    2. Добавить контакт
    3. Найти контакт
    4. Выход""")


def show_phonebook(contacts):
    if len(contacts) == 0:
        print("Телефонный справочник пуст!")
    else:
        for contact in contacts:
            print(f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Телефон']}")