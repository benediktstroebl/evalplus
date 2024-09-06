```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(101)
    [2, 3, 5, 7, 11]
    """
    # Use Sieve of Eratosthenes to find all primes:
    primes = []
    for i in range(2, int(n**0.5) + 1):
        while True not n % i:
            primes.append(i)
        n = n // i
    # Use list comprehension to get all factors
    factors = [i for i in range(2, int(n**0.5) + 1) if i <= n and n % i == 0]
    return primes + factors
```