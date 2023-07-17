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
        user_call = input('вот что я могу показать тебе! Напиши цифру.\n'
                          '1 - список всех компаний и количество вакансий у каждой\n'
                          '2 - список вакансий, название компании, зп, ссылка на вакансию\n'
                          '3 - показать среднюю зп по вакансиям\n'
                          '4 - вакансии с зп выше среднего по всем вакансиям\n'
                          '5 - вакансии со словом ключевому слову\n'
                          'Для выхода введи стоп\n')

        if user_call == '1':
            information.get_companies_and_vacancies_count()
            next_ques = input("Показать что-нибудь еще?")
            if next_ques.lower() == 'да' or next_ques.lower() == 'lf':
                continue
            else:
                break

        elif user_call == '2':
            information.get_all_vacancies()
            next_ques = input("Показать что-нибудь еще?")
            if next_ques.lower() == 'да' or next_ques.lower() == 'lf':
                continue
            else:
                break


        elif user_call == '3':
            information.get_avg_salary()
            next_ques = input("Показать что-нибудь еще?")
            if next_ques.lower() == 'да' or next_ques.lower() == 'lf':
                continue
            else:
                break

        elif user_call == '4':
            information.get_vacancies_with_higher_salary()
            next_ques = input("Показать что-нибудь еще?")
            if next_ques.lower() == 'да' or next_ques.lower() == 'lf':
                continue
            else:
                break

        elif user_call == '5':
            word = input("Введите ключевое слово: ")
            information.get_vacancies_with_keyword(word)
            next_ques = input("Показать что-нибудь еще?")
            if next_ques.lower() == 'да' or next_ques.lower() == 'lf':
                continue
            else:
                break

        elif user_call == 'stop' or user_call == 'cnjg' or user_call == 'стоп':
            break

        else:
            print('Не понимаю тебя')
            input('Начнем снова, нажми enter')

if __name__ == '__main__':
    main()