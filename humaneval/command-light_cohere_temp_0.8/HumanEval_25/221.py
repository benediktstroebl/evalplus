```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many times it appears in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(16)
    [2, 2, 2, 2]
    >>> factorize(100)
    [2, 2, 5, 5, 5]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(2)
    n = n
    while n > 1:
        d = 0
        while d < n // d + 1:
            d += 1
        factors.append(d)
        n = n // d
    return factors
```