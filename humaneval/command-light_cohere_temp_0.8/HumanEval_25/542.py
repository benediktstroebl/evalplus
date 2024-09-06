```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Keep track of the factors that are found, and return them in order from lowest to highest.
    """
    def sieve_prime(n: int) -> List[int]:
        factors = []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5):
            if is_prime[i] == True:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        for i in range(2, n+1):
            if is_prime[i] == True:
                factors.append(i)
        return factors
    """
def factorize(n: int) -> List[int]:
    return sieve_prime(n)
``` 
This script provides a function `factorize` that uses the `sieve_prime` helper function to find and return the prime factors of a given number.  It's work flow of the script is to define a function `factorize` that calls the `sieve_prime` function to get the prime factors of a given number, and then return the list of factors.