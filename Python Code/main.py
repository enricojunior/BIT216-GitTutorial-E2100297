import unittest

def calcAvg(num):
    if not num:
        return 0
    return sum(num) / len(num)

class test_Average(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(calcAvg([5]), 5)
        
    def test_positive_elements(self):
        self.assertEqual(calcAvg([1, 2, 3, 4, 5]), 3)

    def test_empty_list(self):
        self.assertEqual(calcAvg([]), 0)

    def test_negative_elements(self):
        self.assertEqual(calcAvg([-1, -2, -3]), -2)

if __name__ == '__main__':
    unittest.main()