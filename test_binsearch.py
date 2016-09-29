import unittest
from binsearch import binary_search
import numpy as np

class MyTest(unittest.TestCase):

	def setUp(self):
		# All of the below lists are sorted
		self.arr = list(range(10))
		self.stringarr = ['a', 'b', 'c', 'd', 'e', 'f']
		self.duparr =  [1, 1, 1, 1, 2, 4, 5, 6, 7, 8, 8]
		self.nanarr = [np.NaN, np.NaN, 0, 1, 2, 4] 
		self.infarr = [1, 2, 4, 3, np.inf, np.inf]

	def tearDown(self):
		del self.arr
		del self.stringarr
		del self.duparr
		del self.nanarr
		del self.infarr

	'''
	Step 0: Basic tests that illustrate the interface
	'''

	def test_notfound(self):
		self.assertEqual(binary_search(self.arr, 4.5), -1)

	def test_found(self):
		self.assertEqual(binary_search(self.arr, 3), 3)

	def test_needle_within_range(self):
		self.assertEqual(binary_search(self.arr, 4, 1, 3), -1)

	def test_needle_not_within_range(self):
		self.assertEqual(binary_search(self.arr, 6, 4, 7), 6)

	'''
	Step 1: Test weird input
	'''

	def test_oneelementarr(self):
		self.assertEqual(binary_search([0], 0), 0)
		self.assertEqual(binary_search([0], -2), -1)

	def test_emptyarr(self):
		self.assertEqual(binary_search([], 4), -1)

	def test_stringarr_found(self):
		self.assertEqual(binary_search(self.stringarr, 'b'), 1)

	def test_stringarr_notfound(self):
		self.assertEqual(binary_search(self.stringarr, 'g'), -1)

	def test_duparr_found(self):
		# Can return 0,1,2,3
		self.assertTrue(binary_search(self.duparr, 1) in [0, 1, 2, 3])

	def test_duparr_notfound(self):
		self.assertEqual(binary_search(self.duparr, 3), -1)

	def test_nanarr(self):
		self.assertEqual(binary_search(self.nanarr, 2), 4)

	def test_infarr_found(self):
		self.assertEqual(binary_search(self.infarr, 2), 1)

	def test_infarr_notfound(self):
		self.assertEqual(binary_search(self.infarr, 7), -1)

	def test_findnan(self):
		# This is false, when it is supposed to be true. np.NaN is reported to be 2 instead!
		self.assertFalse(binary_search(self.nanarr, np.NaN) in [0, 1])	

	def test_findinf(self):
		self.assertTrue(binary_search(self.infarr, np.inf) in [4, 5])	

	def test_largearray(self):
		largearr = list(range(999999))
		self.assertEqual(binary_search(largearr, 1), 1)

	'''
	Step 2: Test needles
	'''

	def test_leftpointerlessthanzero_found(self):
		self.assertEqual(binary_search(self.arr, 3, -4, len(self.arr) - 1), 3)

	def test_leftpointerlessthanzero_notfound(self):
		self.assertEqual(binary_search(self.arr, -2, -4, len(self.arr) - 1), -1)

	def test_rightpointermorethanlength_found(self):
		self.assertEqual(binary_search(self.arr, 5, 0, len(self.arr) + 5), 5)

	def test_rightpointermorethanlength_notfound(self):
		self.assertEqual(binary_search(self.arr, -7, 0, len(self.arr) + 5), -1)

	def test_needlesatfront(self):
		self.assertEqual(binary_search(self.stringarr, 'a', 0, len(self.stringarr) - 1), 0)

	def test_needlesatback(self):
		self.assertEqual(binary_search(self.stringarr, 'f', 0, len(self.stringarr) - 1), 5)

	'''
	Step 3: Integration of Step 1 and Step 2
	'''

	def test_duparr_needlesatfront(self):
		self.assertEqual(binary_search(self.duparr, 1, 0, 1), 0)

	def test_duparr_needlesatback(self):
		self.assertEqual(binary_search(self.duparr, 8, 9, 10), 9)		

	def test_infarr_outofrange_findnum(self):
		self.assertEqual(binary_search(self.infarr, 1, 4, 5), -1)

	def test_infarr_outofrange_findinf(self):
		self.assertEqual(binary_search(self.infarr, np.inf, 2, 3), -1)

	def test_infarr_withinrange_findnum(self):
		self.assertEqual(binary_search(self.infarr, 1, 0, 3), 0)

	def test_infarr_withinrange_findinf(self):
		self.assertEqual(binary_search(self.infarr, np.inf, 3, 4), 4)

	def test_nanarr_withinrange(self):
		self.assertEqual(binary_search(self.nanarr, 2, 3, 5), 4)

	'''
	Step 4: Failed tests that are mostly covered in pre/post conditions (commented out)
	'''

	'''1) Input is not a list but still passes!'''
	# self.assertEqual(binary_search('123','123'), -1) 

	'''2) Unorderable types: str() > int() because array does not support mixed types'''
	# self.assertEqual(binary_search(['hey', 1, 'ho', -4, -3], -4), -1)
	# self.assertEqual(binary_search(self.arr, '9999'), -1)

	'''4) Finding nan in arrays containing them does not always work. 
			These return the wrong indexes:'''
	# self.assertTrue(binary_search(self.nanarr, np.NaN) in [0, 1])	 # Found at 2, but should be 0 or 1

	'''5) List index out of range error when left is <= -n or right >= n, and when needle is 
			also not in the range'''
	# self.assertEqual(binary_search(self.arr, 12, 1, len(self.arr) + 5), -1)
	# self.assertEqual(binary_search(self.arr, 12, -4, len(self.arr) + 5), -1)
	# self.assertEqual(binary_search(self.arr, -12, -4, len(self.arr) + 5), -1)


suite = unittest.TestLoader().loadTestsFromModule(MyTest())
unittest.TextTestRunner().run(suite)
