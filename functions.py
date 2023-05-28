def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='UTF-8') as file:
        print(file.read())  


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        book = file.read().lower()
    data_to_find = input('Введите искомые данные: ').lower()
    matches = search(book, data_to_find)
    if type(matches) == list:
        for match in matches:
            print('\n'+ match.title())
    else:
        print('\n'+ matches.title())
    
    answer = input('\n' + 'Нужно ли уточнить поиск? (Да/Нет): ')
    if answer.lower() == 'да':
        print('\n')
        print('\n' + finer_search(matches, input('Уточните искомые данные: '+'\n')).title() + '\n')


def finer_search(data: str, info: str) -> str:
    '''Ищет в результатах поиска по уточнению пользователя'''
    for contact in data:
        if info in contact:
            return contact
    return 'Совпадений не найдено.'


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    matches = []
    for contact in book:
        if info in contact:
            matches.append(contact)
    if len(matches) == 0:
        return 'Совпадений не найдено.'
    elif len(matches) == 1:
        return matches[0]
    else:
        return matches
    

