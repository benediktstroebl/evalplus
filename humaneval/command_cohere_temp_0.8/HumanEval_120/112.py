Here's a Python script that contains a function to solve the problem and exemplar tests:
```python
# The following code is dedicated to rigorously testing the 'maximum' function
import unittest

# The function to be tested
def maximum(arr, k):
    # Sort the list in ascending order
    arr.sort()
    return arr[:k]


# Create a class to test the function 'maximum'
class TestMaximum(unittest.TestCase):
    # Set up a list of test cases
    def test_max1(self):
        arr = [-3, -4, 5]
        k = 3
        result = maximum(arr, k)
        self.assertEqual(result, [-4, -3, 5])

    def test_max2(self):
        arr = [4, -4, 4]
        k = 2
        result = maximum(arr, k)
        self.assertEqual(result, [4, 4])

    def test_max3(self):
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        result = maximum(arr, k)
        self.assertEqual(result, [2])

    def test_max4(self):
        arr = [1, 5, 3, 6, 2, 4, 8]
        k = 4
        result = maximum(arr, k)
        self.assertEqual(result, [6, 5, 8, 4])

    def test_max5(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        k = 3
        result = maximum(arr, k)
        self.assertEqual(result, [8, 6, 5])

    def test_max6(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        k = 6
        result = maximum(arr, k)
        self.assertEqual(result, [8, 7, 6, 5, 4, 3])

    def test_max7(self):
        arr = [1]
        k = 1
        result = maximum(arr, k)
        self.assertEqual(result, [1])

    def test_max8(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        k = 2
        result = maximum(arr, k)
        self.assertEqual(result, [8, 7])

    def test_max9(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k = 3
        result = maximum(arr, k)
        self.assertEqual(result, [9, 8, 7])

    def test_max10(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 4
        result = maximum(arr, k)
        self.assertEqual(result, [10, 9, 8, 7])

    def test_max11(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 11
        result = maximum(arr, k)
        self.assertEqual(result, [10, 9, 8, 7, 6, 5])

    def test_max12(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        k = 12
        result = maximum(arr, k)
        self.assertEqual(result, [11, 10, 9, 8, 7,