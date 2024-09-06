```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the number itself and also the number of times it appears in factorization.
    >>> factorize(8)
    [2, 2]
    >>> factorize(25)
    [5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    """
    factors = []
    while n % 2 == 0:
        factors.append(n // 2
    n // 2)
    n = n // 2
    while n > 1:
        factors.append(n)
        n // 2
        n = n // 2
    for x in factors:
        assert x == int(x), "Invalid prime factor"
    return factors
```