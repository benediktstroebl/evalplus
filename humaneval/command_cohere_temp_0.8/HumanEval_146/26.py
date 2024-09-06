```python
def specialFilter(nums):
    odd_digits = [x for x in nums if int(x) > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1]
    return len(odd_digits)
```

This function `specialFilter` takes an array of numbers (`nums`) as input and returns the number of elements in the array that are greater than 10 and have odd first and last digits. To achieve this, it iterates through each number in the `nums` array and checks if it satisfies the given conditions. 

To test this function, you can run the following code:
```python
import unittest

class TestSpecialFilter(unittest.TestCase):
    def test_specialFilter(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
    def test_specialFilter_with_negative_numbers(self):
        # Test with negative numbers
        self.assertEqual(specialFilter([15, -73, 14, -15, -321, -53, -91]), 3)
    def test_specialFilter_with_single_digit_numbers(self):
        # Test with single-digit numbers
        self.assertEqual(specialFilter([7, 1, 3, 5, 7]), 0)
    def test_specialFilter_with_large_numbers(self):
        # Test with large numbers
        self.assertEqual(specialFilter([123, 45, 654, 796, 919]), 2)
    def test_specialFilter_with_no_numbers(self):
        # Test with an empty list
        self.assertEqual(specialFilter([]), 0)

if __name__ == '__main__':
    unittest.main()
```

This code snippet wraps the function inside a `unittest` module, which is a standard Python testing framework. It runs a series of test cases with varying inputs to ensure that the `specialFilter` function produces the expected results for different scenarios. 

This way, when you run the script, the `unittest` module automatically executes all the test cases and reports whether the function's outputs match the expected values.