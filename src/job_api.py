import requests
import json


class API:
    @staticmethod
    def filter_vacancies(vacancies):
        filtered_vacancies = '+'.join(vacancies)
        return filtered_vacancies


class HeadHunterAPI(API):
    @staticmethod
    def get_vacancies(fvacancies, top):
        fvacancies = API.filter_vacancies(fvacancies)
        req = requests.get(f'https://api.hh.ru/vacancies?page=0&per_page=20&text={fvacancies}&order_by=salary_desc&only_with_salary=true')
        data = req.content.decode()
        req.close()
        vacancies = json.loads(data)
        for i in range(top):
            if len(vacancies['items']) < 1:
                print('Вакансии не найдены')
                break
            elif len(vacancies['items']) - 1 < i:
                break
            else:
                print(f'{vacancies["items"][i]}')


class SuperJobAPI(API):
    @staticmethod
    def get_vacancies(fvacancies, top):
        fvacancies = API.filter_vacancies(fvacancies)
        req = requests.get(f'https://api.superjob.ru/2.0/vacancies?order_field=payment&no_agreement=1&keyword={fvacancies}', headers={'X-Api-App-Id':'v3.r.120653557.c8c74b7e151674eebf849f62b090cce612422b12.f58a2161d721af963c032b3902d89288cad4feab'})
        data = req.content.decode()
        req.close()
        vacancies = json.loads(data)
        for i in range(top):
            if len(vacancies['objects']) < 1:
                print('Вакансии не найдены')
                break
            elif len(vacancies['objects'])-1 < i:
                break
            else:
                print(f'{vacancies["objects"][i]}')