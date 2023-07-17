from src.config import config
from src.utils import get_hhRU_data, create_database, save_data_to_database
from src.connect_database import DBManager


def main():
    company_ids = ['4117901', '1740', '8582', '242319', '1942330', '1582752',
                   '4657939', '60377', '9163125', '176941'
                   ]
    params = config()

    data = get_hhRU_data(company_ids)  # получение данных с HH_ru
    create_database('kursovaya5', params)
    save_data_to_database(data, 'kursovaya5', params)

    information = DBManager(params)

    while True:
        while True:  # проверка ответа пользователя

            human_response = input("Могу показать список всех компаний и количество их вакансий? Да/Нет"
                                   "\nОтвет: ")

            if human_response.lower() == 'да':
                information.get_companies_and_vacancies_count()
                break

            if human_response.lower() == 'нет':
                break
            else:
                print('Неверно введен ответ на вопрос')
                continue

        while True:
            human_response = input("Вывести на экран список всех вакансий с указанием названия компании,"
                                   "названия вакансии и зарплаты и ссылки на вакансию? Да/Нет"
                                   "\nОтвет: ")
            if human_response.lower() == 'да':
                information.get_all_vacancies()
                break
            if human_response.lower() == 'нет':
                break
            else:
                print('Неверно введен ответ на вопрос')
                continue

        while True:
            human_response = input("Вывести на экран среднюю зарплату по вакансиям? Да/Нет"
                                   "\nОтвет: ")
            if human_response.lower() == 'да':
                information.get_avg_salary()
                break
            if human_response.lower() == 'нет':
                break
            else:
                print('Неверно введен ответ на вопрос')
                continue

        while True:
            human_response = input("Вывести на экран список всех вакансий, у которых "
                                   "зарплата выше средней по всем вакансиям? Да/Нет"
                                   "\nОтвет: ")
            if human_response.lower() == 'да':
                information.get_vacancies_with_higher_salary()
                break
            if human_response.lower() == 'нет':
                break
            else:
                print('Неверно введен ответ на вопрос')
                continue

        while True:
            human_response = input("Вывести на экран список всех вакансий, в названии "
                                   "которых содержатся слова, например “python”? Да/Нет"
                                   "\nОтвет: ")
            if human_response.lower() == 'да':
                word = input("Введите слово: ")
                information.get_vacancies_with_keyword(word)
                exit()
            if human_response.lower() == 'нет':
                exit()
            else:
                print('Неверно введен ответ на вопрос')
                continue


if __name__ == '__main__':
    main()