from job_api import SuperJobAPI, HeadHunterAPI, API
from vacancy import Vacancy, JSONSaver

'''Функция взаимодействия с пользователем через консоль'''
def user_interaction():
    answer = input(
        'Выберите платформу с вакансиями\nВарианты:\n1. HeadHunter\n2. SuperJob\n3. Искать на всех платформах\n')
    if answer == "1":
        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        filter_words.insert(0, search_query)
        HeadHunterAPI.get_vacancies(filter_words, top_n)
    elif answer == "2":
        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        filter_words.insert(0, search_query)
        SuperJobAPI.get_vacancies(filter_words, top_n)
    else:
        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
        filter_words.insert(0, search_query)
        HeadHunterAPI.get_vacancies(filter_words, top_n)
        SuperJobAPI.get_vacancies(filter_words, top_n)




if __name__ == '__main__':
    user_interaction()

    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/123456", "100 000-150 000 руб.",
                         "Требования: опыт работы от 3 лет...")

    json_saver = JSONSaver()
    json_saver.to_json(vacancy)
    json_saver.delete_vacancy(vacancy)
    json_saver.get_vacancy_by_name('Python Developer')

