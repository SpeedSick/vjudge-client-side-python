import json
import yaml

from requests import get, post

URL = 'http://0.0.0.0:5000/'


class Test:

    def __init__(self):
        self.__score = 0
        self.__data__ = {}
        self.__expected_answer__ = {}

    def get_data(self):
        return self.__data__

    def get_expected_answer(self):
        return self.__expected_answer__

    def run(self):
        print(URL)
        print(self.get_data())
        response = post(URL, data=self.get_data())
        self.check_response(response)

    def check_response(self, response):
        print(response)
        print(json.dumps(response.json()))
        if response.status_code == 200 and response.json() == self.get_expected_answer():
            self.__score__ = 1
        else:
            self.__score__ = 0

    def get_score(self):
        return self.__score__

    def load(self, name, data):
        self.__data__ = data.get('data', {})
        self.__expected_answer__ = data.get('expected_answer', {})
        self.__score__ = 0

    def __str__(self):
        return "data is {data}\nexpected_answer is {answer}\nscore is {score}".format(
            data=json.dumps(self.get_data()),
            answer=json.dumps(self.get_expected_answer()),
            score=self.get_score(),
        )


def load_tests():
    data = yaml.load(open("tests.yml", 'r').read())

    tests = []

    for test_name, test_data in data.items():
        test = Test()
        test.load(test_name, test_data)
        tests.append(test)

    return tests


def run():
    tests = load_tests()

    score = 0

    for test in tests:
        test.run()
        score += test.get_score()

    return score
