Here's a Python script that includes a function to solve the given problem:
```python
def solve(n):
    """
    :param n: Integer to be converted to binary sum of digits
    :return: String - Binary string of the sum of digits of n
    """
    total_sum = sum(map(int, str(n)))
    return format(total_sum, 'b')
```

This script defines a function `solve(n)` that takes an integer `n` as its parameter and calculates the sum of its digits. It uses the `sum()` function to calculate the sum of the digits extracted using `map(int, str(n))`. Finally, it employs the `format()` function to convert the integer sum into a binary string, which is then returned. 

The unit tests for this function can be run as follows:
```python
# Imports - Needed for testing
import unittest

# Problem Solution - Import only from this script
from solve_binary_sum_of_digits import solve

# Testing
class TestBinarySumOfDigits(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(solve(0), "0")

    def test_one(self):
        self.assertEqual(solve(1), "1")

    def test_small_numbers(self):
        self.assertEqual(solve(10), "2")
        self.assertEqual(solve(12), "110")

    def test_large_numbers(self):
        self.assertEqual(solve(987), "11011000")
        self.assertEqual(solve(147), "1101100")
        self.assertEqual(solve(1000), "1")

if __name__ == '__main__':
    unittest.main()
``` 

This test suite includes test cases for various inputs, encompassing zero, small, and large numbers to ensure the accuracy of the `solve()` function in determining the binary sum of digits for different cases.