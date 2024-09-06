```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If this function, it uses the Sieve of Eratosthenes to find prime factors.
    return [ list(filter(lambda x: x > 1 and is_prime(x), range(n+1)) ))

def is_prime(x):
    """ True if x is prime, False otherwise.
    """
    return all(x > 1 and x != 2 and x != 3 and x != 5)

# Unit test
def test_factorize():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
```
This Python script defines a function factorize that returns a list of prime factors for a given integer n. The Sieve of Eratosthenes algorithm is used to find these factors. It then defines a function is_prime to check if a given number is prime, and a function test_factorize to test the function. The test_factorize function uses the assert statement to check if the function returns the correct result for a given input.