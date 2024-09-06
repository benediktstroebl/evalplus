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
    >>> factorize(77)
    [7, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(111)
    [3, 3, 3]
    >>> factorize(9223372036854775807)
    [19, 19, 19]
    """
    # Use sieve of Eratosthenes to find prime factors
    factors = []
    limit = int(n**0.5)
    prime_factors = [True] * (limit + 1)
    prime_factors[0] = False  # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        while prime_factors[i] == True:
            for j in range(i * i, limit + 1, i):
                prime_factors[j] = False
        for j in range(limit + 1):
            if prime_factors[j]:
                factors.append(j)
    # Return list of prime factors
    return factors
```