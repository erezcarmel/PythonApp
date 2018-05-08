import unittest
from app import hello_world


class TestApp(unittest.TestCase):

    def test_hello_world(self):
        print('hello_world')
        self.assertEqual(hello_world(), 'Hello world!')


if __name__ == '__main__':
    unittest.main()
