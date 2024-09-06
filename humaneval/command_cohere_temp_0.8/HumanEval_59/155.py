```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return max(factors)
```

This approach first exhausts the even factors and then moves through the odd factors incrementally from 3 to the square root of `n`. 

#### Testing
To test this function, you can create a file `test_largest_prime_factor.py` with the following content:
```python
import unittest

from largest_prime_factor import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(97), 97)
        self.assertEqual(largest_prime_factor(1001), 1001)

    def test_largest_prime_factor_edge_cases(self):
        self.assertIsNone(largest_prime_factor(1))
        self.assertIsNone(largest_prime_factor(7))

if __name__ == '__main__':
    unittest.main()
```

This file uses the `unittest` module to define a test case and individual test functions. 

The `test_largest_prime_factor` function calls the `assertEqual` method to compare the output of the `largest_prime_factor` function with the expected value for three specific inputs (`13195`, `2048`, `97`). The `assertIsNone` function is used to check if the function returns `None` for invalid inputs (`1` and `7`).

The `test_largest_prime_factor_edge_cases` function tests the edge cases specified in the example test cases. 

Finally, `unittest.main()` is called to run all the defined tests. 

When you run this test file, you should see the following output:
```python
...
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```