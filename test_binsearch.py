import unittest
from binsearch import binary_search
from pytest import fixture


class MyTest(unittest.TestCase):

	# def setUp(self):
		# self.arr = list(range(10))

	def setUp(self):
		self.arr = list(range(10))

	def test_notfound(self):
		self.assertEqual(binary_search(self.arr, 4.5), -1)

	def test_found(self):
		self.assertEqual(binary_search(self.arr, 3), 3)

suite = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(suite)
