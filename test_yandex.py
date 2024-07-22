from unittest import TestCase
from yandex import create_folder


class TestCreateFolder(TestCase):

    def test_status_code1(self):
        code = 201
        result = create_folder('Фото')
        self.assertEqual(code, result.status_code)

    def test_status_code2(self):
        code = 409
        result = create_folder('Фото')
        self.assertEqual(code, result.status_code)

    def test_status_code3(self):
        code = 401
        result = create_folder('Фото')
        self.assertEqual(code, result.status_code)