```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```
The function `is_multiply_prime` checks if a given number is the multiplication of three prime numbers. It first calculates the factors of the number and then checks if their number is exactly three and that the maximum factor is among the known prime numbers less than 100. The function is initialized with the list of the first primes for convenience. 

Here is how to use it in the script:
```python
import unittest

def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes

class TestIsMultiplyPrime(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(33))
        self.assertTrue(is_multiply_prime(49))

    def test_false(self):
        self.assertFalse(is_multiply_prime(28))
        self.assertFalse(is_multiply_prime(16))
        self.assertFalse(is_multiply_prime(36))
        self.assertFalse(is_multiply_prime(64))

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `unittest` module is used to define unit tests. The `test_true` function tests multiple examples where `is_multiply_prime` is expected to return `True`, and the `test_false` function tests examples where it's expected to return `False.` Finally, `unittest.main()` executes the tests when the script is run directly. 

The code coverage is acceptable but not perfect, as some edge cases aren't accounted for. You can improve it by adding more tests or modifying the existing ones.