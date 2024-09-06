```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return not any(x in factors for x in primes)
```

The function `is_multiply_prime` checks if the given number is the product of 3 or more prime numbers. The first step is to list the known prime numbers (`primes`), and then the function checks if the number is divisible by any number from 1 to its square root. If any of these divisors are prime, the function returns `False`, if none of them are prime, the function returns `True`. The function's complexity is O(Sqrt(N)) where N is the number inputted into the function. 

Here is a testing framework to ensure the functionality of the program:
```python
import unittest

def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return not any(x in factors for x in primes)

class TestIsMultiplyPrime(unittest.TestCase):
    def test_multiply_prime_true(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(51))
        self.assertTrue(is_multiply_prime(74))

    def test_multiply_prime_false(self):
        self.assertFalse(is_multiply_prime(6))
        self.assertFalse(is_multiply_prime(8))
        self.assertFalse(is_multiply_prime(10))

    def test_edge_cases(self):
        self.assertTrue(is_multiply_prime(1))
        self.assertTrue(is_multiply_prime(3))
        self.assertTrue(is_multiply_prime(33))
        self.assertTrue(is_multiply_prime(49))
        self.assertTrue(is_multiply_prime(64))
        self.assertTrue(is_multiply_prime(81))

if __name__ == '__main__':
    unittest.main()
```

This testing framework uses `unittest` to organize and run tests. `unittest` provides a class called `TestCase` which provides a set of methods to create test cases. In the code above, the method `test_multiply_prime_true()` tests examples that should return true, and `test_multiply_prime_false()` tests examples that should return false. `test_edge_cases()` gives edge examples to ensure the function is correct. Finally, the `unittest.main()` method runs all the defined tests.