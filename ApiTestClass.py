import requests
import unittest


# Class for testing the functionality of the given api
class ApiTestClass(unittest.TestCase):
    # setup function that preparing a new access token and a test json before each test case
    def setUp(self):
        res = requests.post('http://localhost:8000/api/auth', json={"username": "test", "password": "1234"})
        self.headers = {'Content-type': 'application/json',
                        'Authorization': f'Bearer {res.json()["access_token"]}'}

        self.test_json = {"data": [
                    {
                        "key": "key1",
                        "val": "val1",
                        "valType": "str"
                    }
                ]}

    # Checking the GET method for returning a list object
    def test_get_method(self):
        res = requests.get('http://localhost:8000/api/poly',
                           headers=self.headers)
        self.assertEqual(isinstance(res.json(), list), True, 'Should be true')

    # Checking the POST and GET methods in a new object insert scenario
    def test_insertion(self):
        post_res = requests.post('http://localhost:8000/api/poly',
                                 headers=self.headers,
                                 json=self.test_json)

        get_res = requests.get(f'http://localhost:8000/api/poly/{post_res.json()["id"]}',
                               headers=self.headers)
        self.assertEqual(post_res.json()["id"], get_res.json()["object_id"], 'Should be true')
        self.assertEqual(post_res.json()["values"], get_res.json()["data"], 'Should be true')

    # Checking the POST, DELETE and GET methods in a object deleting scenario
    def test_deletion(self):
        post_res = requests.post('http://localhost:8000/api/poly',
                                 headers=self.headers,
                                 json=self.test_json)

        delete_res = requests.delete(f'http://localhost:8000/api/poly/{post_res.json()["id"]}',
                                     headers=self.headers)

        get_res = requests.get(f'http://localhost:8000/api/poly/{post_res.json()["id"]}',
                               headers=self.headers)

        self.assertEqual(get_res.json()["error"], 'Not Found', 'Should be true')
        self.assertEqual(delete_res.status_code, 200, 'Should be true')


if __name__ == '__main__':
    unittest.main()
