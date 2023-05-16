import unittest

from main import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_form_route_with_post_request_and_option1(self):
        response = self.client.post('/', data={'summ': '2000000', 'first_installment': '500000', 'month': '15',
                                               'percent': '12', 'gridRadios': 'option1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytes("Ежемесячный платёж:", encoding='utf-8'), response.data)
        self.assertIn(bytes('Cумма кредита:', encoding='utf-8'), response.data)

    def test_form_route_with_post_request_and_option2(self):
        response = self.client.post('/', data={'summ': '2000000', 'first_installment': '500000', 'month': '15',
                                               'percent': '12', 'gridRadios': 'option2'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(bytes("Ежемесячный платёж:", encoding='utf-8'), response.data)
        self.assertIn(bytes('Cумма кредита:', encoding='utf-8'), response.data)

    def test_form_route_with_get_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    if __name__ == '__main__':
        unittest.main()
