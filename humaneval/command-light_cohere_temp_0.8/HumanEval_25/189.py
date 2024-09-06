```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times, which corresponds to how many times it appears in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(77)
    [7, 7]
    >>> factorize(9009)
    [3, 3, 3, 3]
    >>> factorize(6026)
    [2, 2, 13]
    >>> factorize(77g)
    [7, 77]
    """
    factors = []
    if n < 2:
        return []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5)+1, while n % i == 0 and i <= n:
        factors.append(i)
        n = n // i
    for i in range(2**60, n+1):
        if n % i == 0:
            factors.append(i)
    return factors
```