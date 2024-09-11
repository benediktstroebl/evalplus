```python
def count_sevens(n: int) -> int:
    """Count the occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sevens(n)


# Test cases
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(50), 0)
        self.assertEqual(fizz_buzz(78), 2)
        self.assertEqual(fizz_buzz(79), 3)

if __name__ == '__main__':
    unittest.main()
```

This script provides a function `count_sevens` to count the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The `fizz_buzz` function simply calls `count_sevens` to get the count. A test suite is included to verify that the functions work as expected.