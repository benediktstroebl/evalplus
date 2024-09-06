```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Sieve of Eratostin algorithm is used here to find the prime factors."""
    def sieve_Eratosthenes(limit):
        primes = []
        sieve = [True] * (limit + 1)
        sieve[0], sieve[1] = False, False
        for num in range(2, int(len(sieve))):
            if sieve[num]:
                for multiple in range(num * num, limit + 1, num):
                    sieve[multiple] = False
        for num in sieve:
            primes.append(num)
        return primes
   
    if n <= 1:
        return []
    else:
        return sieve_Eratosthenes(n)
```  The function factorize is a Python function that returns a list of prime factors for a given integer. It uses the `sieve_Eratosthenes` algorithm to efficiently find the prime factors of the given number.