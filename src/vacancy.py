import json


class Vacancy:
    '''Класс представляющий сущность - вакансия'''
    def __init__(self, name, link, salary, requirements):
        if name != '':
            self.name = name
        else:
            raise AttributeError('Неправильно задано имя')
        if link != '':
            self.link = link
        else:
            raise AttributeError('Неправильно задана ссылка')
        if salary != '':
            self.salary = salary
        else:
            raise AttributeError('Неправильно задана зарплата')
        if requirements != '':
            self.requirements = requirements
        else:
            raise AttributeError('Неправильно заданы требования')

    '''Перегрузка операторов сравнения класса'''
    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary


class JSONSaver:
    '''Класс для сохранения информации и взаимодействия с файлом в формате json '''
    @staticmethod
    def to_json(vacancy):
        data = {
            "name": vacancy.name,
            "link": vacancy.link,
            "salary": vacancy.salary,
            "requirements": vacancy.requirements
        }

        try:
            with open('vacancies.json', 'r') as f:
                data_r = json.load(f)
                f.close()
            data_r['items'].append(data)
        except Exception:
            with open('vacancies.json', 'w') as f:
                f.write('{"items":[]}')
                f.close()
            with open('vacancies.json', 'r') as f:
                data_r = json.load(f)
                f.close()
                data_r['items'].append(data)
        with open('vacancies.json', 'w') as f:
            json.dump(data_r, f, ensure_ascii=False, indent=4)

    '''Получение вакансии по названию'''
    @staticmethod
    def get_vacancy_by_name(name):
        with open('vacancies.json', 'r') as f:
            data_r = json.load(f)
            f.close()
        for i in data_r['items']:
            if i['name'] == name:
                print(f"{i['name']}, {i['link']}, {i['salary']}, {i['requirements']}")

    '''Удаление вакансии'''
    @staticmethod
    def delete_vacancy(vacancy):
        data = {
            "name": vacancy.name,
            "link": vacancy.link,
            "salary": vacancy.salary,
            "requirements": vacancy.requirements
        }
        with open('vacancies.json', 'r') as f:
            data_r = json.load(f)
            f.close()
        data_r['items'].remove(data)
        with open('vacancies.json', 'w') as f:
            json.dump(data_r, f, ensure_ascii=False, indent=4)