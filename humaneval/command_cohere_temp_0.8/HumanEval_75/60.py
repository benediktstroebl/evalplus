```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = set(primes[i:] for i in range(len(primes)) if a % primes[i] == 0)
    return len(divisors) == 3
```

The function `is_multiply_prime` checks if the number is divisible by any primes and if the set of divisors has exactly 3 elements, it returns `True`. 

The test cases can be run with:
```python
import unittest

class TestIsMultiplePrime(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_multiply_prime(30))

    def test_false(self):
        self.assertFalse(is_multiply_prime(24))
        self.assertFalse(is_multiply_prime(28))
        self.assertFalse(is_multiply_prime(32))

if __name__ == '__main__':
    unittest.main()
```

The test suite contains three tests, one for the example provided, and two additional ones for false cases.