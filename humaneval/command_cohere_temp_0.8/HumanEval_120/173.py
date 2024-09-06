Here's a Python script that includes a function maximum_k to solve the problem, along with a set of unit tests to verify its correctness:
```python
import unittest

def maximum_k(arr, k):
    """
    Finds the maximum k numbers from the array arr and returns a sorted list of length k.
    """
    arr = sorted(arr)
    return arr[:k]

class MaximumKTest(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(maximum_k([-3, -4, 5], 3), [-4, -3, 5])

    def test_example_2(self):
        self.assertEqual(maximum_k([4, -4, 4], 2), [4, 4])

    def test_example_3(self):
        self.assertEqual(maximum_k([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_large_array(self):
        self.assertEqual(maximum_k([50000, 10000, 5000, 1000, 100, 10, 1], 3), [50000, 10000, 5000])

    def test_small_k(self):
        self.assertEqual(maximum_k([2, 3, 4, 9, 10], 2), [9, 10])

    def test_large_k(self):
        self.assertEqual(maximum_k([1, 2, 3, 4, 5], 10), [3, 4, 5])

    def test_empty_array(self):
        self.assertEqual(maximum_k([], 10), [])

    def test_only_one_element(self):
        self.assertEqual(maximum_k([10], 10), [10])

    def test_negative_k(self):
        self.assertEqual(maximum_k([1, 2, 3, 4, 5], -2), [])

    def test_k_greater_than_array_length(self):
        self.assertEqual(maximum_k([1, 2, 3], 6), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
```

In this script, the `maximum_k` function takes in an array `arr` and an integer `k` as parameters and returns a sorted list containing the maximum `k` numbers from the array. The unit tests are implemented using the `unittest` module to cover various test cases, including edge cases. 

By running this script, you can validate the correctness of the `maximum_k` function and ensure it passes all the tests. Adjust the script as needed to fulfill any specific requirements or coding standards you may have.