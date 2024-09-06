```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function `is_multiply_prime` checks if the number `n` is the product of three prime numbers. The list `primes` stores prime numbers up to the square root of `n`. The set `factors` stores the distinct factors of `n`. 
The function returns `True` if `len(factors)` is 3 and `factors` contains only prime numbers from the list `primes`.

Here is a test suit to verify the functionality of the `is_multiply_prime` function.
```python
import unittest

def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors

class TestIsMultiplyPrime(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(54))
        self.assertTrue(is_multiply_prime(81))
        self.assertTrue(is_multiply_prime(90))

    def test_invalid(self):
        self.assertFalse(is_multiply_prime(6))
        self.assertFalse(is_multiply_prime(28))
        self.assertFalse(is_multiply_prime(35))
        self.assertFalse(is_multiply_prime(45))
        self.assertFalse(is_multiply_prime(100))

if __name__ == '__main__':
    unittest.main()
```
The test suite has two test functions. The `test_valid` function tests four examples for the function `is_multiply_prime` where the parameter is multiply prime and one empty test to ensure the proper functioning of the code. The `test_invalid` function contains tests for invalid cases where the parameter is not a multiply prime. 

The `unittest.main()` call runs the tests when the script is executed directly. You can use the `find_bugs` and `pylint` tools to control the code quality and discover any issues and bugs. 
To get more code improvement and enhancement suggestions, you can also use the `flake8` tool.