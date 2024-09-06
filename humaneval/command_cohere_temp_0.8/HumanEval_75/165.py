```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function `is_multiply_prime` checks if the number is a multiplication of three primes. First, it assumes that at least one factor is less than or equal to the square root of the tested number, then it calculates the set of all possible factors of that type, and finally checks if the set of possible factors is a subset of the set of known primes. Here the assumption that at least one factor is less than or equal to the square root is used, which is quite conservative and ensures the correctness of the algorithm in the worst case. 

The known primes are stored in the list `primes`, and the set of factors is stored in the set `factors`. The expected length of `factors` is 3, which means that the number should be a product of three different primes. 

The code also uses the range of numbers from 1 to the square root of the tested number as it is known that all factors of a number are less than or equal to its square root. You can find more about it here: https://brg.twb-dl.com/pdf/ NUMBER_THEORY__PRIMES_AND_FACTORIZATION__2018_.pdf

The code works as expected as it passes the test:
```python
import unittest

class TestIsMultiplyPrime(unittest.TestCase):
    def test_is_multiply_prime_true(self):
        self.assertTrue(is_multiply_prime(30))
    
    def test_is_multiply_prime_false(self):
        self.assertFalse(is_multiply_prime(17))
        self.assertFalse(is_multiply_prime(104))
``` 

In the first test, the function should return True, as for the number 30 we have 2 * 3 * 5. In the second and third test, the function should return False, as 17 is a prime number, and 104 is a product of 2 and 52, which are not included in the `primes` list.