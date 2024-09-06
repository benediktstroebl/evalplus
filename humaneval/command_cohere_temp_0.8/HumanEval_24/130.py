```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # largest divisor
            if j < i:
                return j  # return the largest divisor if it's less than n
    return 1  # return 1 if no number divides n fully

# Tests
import unittest

class TestLargestDivisor(unittest.TestCase):
    def test_largest_divisor_15(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_largest_divisor_1(self):
        self.assertEqual(largest_divisor(1), 1)

    def test_largest_divisor_7(self):
        self.assertEqual(largest_divisor(7), 1)

if __name__ == '__main__':
    unittest.main()
```

In this script, the `largest_divisor` function iterates through numbers from 1 to `n`, checking if any number divides `n` fully (i.e., `n % i == 0`). If it finds such a number `i`, it checks if any larger divisors (`n // i`) exist. If they do, this larger divisor `j` is returned. If no number divides `n` fully, `1` is returned. 

The tests ensure that the function behaves correctly for the sample inputs provided. 

Let me know if this solves the problem or if you'd like me to explain any part of the solution in more detail.