import json
import unittest

from app import app


class APITestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        res = tester.get('/')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.data, b'{"error":"404 Not Found"}\n')

    def test_person(self):
        tester = app.test_client(self)
        res = tester.get('/paranaura/api/v1.0/people/562')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['age'], 33)
        self.assertEqual(data['username'], 'Hancock Stone')

    def test_friends(self):
        tester = app.test_client(self)
        res = tester.get('/paranaura/api/v1.0/people/678/520')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['common_friends'], [1, 4])

    def test_company(self):
        tester = app.test_client(self)
        res = tester.get('/paranaura/api/v1.0/company/ZENTRY')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        employees = []
        for item in data:
            employees.append(item['index'])
        self.assertEqual(employees,
                         [4, 27, 49, 105, 113, 265, 408, 421, 456, 473, 515, 528, 587, 640, 687, 793, 836, 979])


if __name__ == '__main__':
    unittest.main()
