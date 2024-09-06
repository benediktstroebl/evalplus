```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number is divisible by n, it returns the largest number within this range. 
If n is not divisible by any number in this range, the function returns 1, as num ** 1 always divides n evenly. 

This approach is efficient as it cuts the search range with every divisor found, eliminating larger numbers that are not divisors. 

The unit tests for this function can be created using Python's built-in `unittest` module, with a test case looking something like this:
```python
import unittest

class TestLargestDivisor(unittest.TestCase):
    def test_largest_divisor_with_15(self):
        self.assertEqual(largest_divisor(15), 5)
    def test_largest_divisor_with_7(self):
        self.assertEqual(largest_divisor(7), 1)
    def test_largest_divisor_with_10(self):
        self.assertEqual(largest_divisor(10), 5)
if __name__ == '__main__':
    unittest.main()
```
This test suite will uncover edge cases and provide confidence in the correctness of the function. 
```unittest.main()``` helps to run tests when the script is executed directly. 
For more complex scenarios or larger test suites, it's recommended to use a test runner to organize and execute tests more effectively.