```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Use the Sieve of Eratosthenes to find prime factors
    factors = []
    for i in range(1, int(n**0.5)):
        if n%i == 0:
            factors.append(i)
            n //= i 
    return factors
```