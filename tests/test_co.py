import unittest

from pyTest import component_one as co

class TestComponentOne(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiply(self):
        self.assertEqual(co.multiply(3, 4), 12)

if __name__ == '__main__':
    unittest.main()

