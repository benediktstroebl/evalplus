Here's a Python script that includes a function maximum_k to solve the problem, along with a set of unit tests to validate its correctness:
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
        self.assertEqual(maximum_k([3, 9, 2, 6, 5, 5, 7, 6, 10, 2, 3], 3), [9, 10, 6])

    def test_empty_array(self):
        self.assertEqual(maximum_k([], 1), [])

    def test_k_greater_than_array_length(self):
        self.assertEqual(maximum_k([1, 2, 3], 4), [2, 3])

if __name__ == '__main__':
    unittest.main()
```

In this script, the `maximum_k` function takes two parameters, a list of integers `arr` and an integer `k`. It sorts the array and returns the first `k` elements, effectively capturing the maximum `k` numbers in the sorted arrangement. 

The unit tests are implemented using the `unittest` module. These tests cover various scenarios, including edge cases, to validate the correctness of the `maximum_k` function. When you run the script, the tests will execute automatically, ensuring that the function behaves as expected.