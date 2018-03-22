import unittest
from primes import is_prime

class SimplisticTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)


class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))


    def test_is_two_prime(self):
        
        self.assertTrue(is_prime(3))



class TruthTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_false(self):
        self.assertFalse(False)

class OutcomesTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)
'''
    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')
'''

if __name__ == '__main__':
    unittest.main()