```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in the factorization
    >>> factors = factorize(8)
    [2, 2, 2]
    >>> factors = factorize(25)
    [5, 5]
    >>> factors = factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    while n % 5 == 0:
        factors.append(5)
        n = n // 5
    while n % 7 == 0:
        factors.append(7)
        n = n // 7
    while n % 11 == 0:
        factors.append(11)
        n = n // 11
    while n % 13 == 0:
        factors.append(13)
        n = n // 13
    while n % 17 == 0:
        factors.append(17)
        n = n // 17
    while n % 19 == 0:
        factors.append(19)
        n = n // 19
    while n % 23 == 0:
        factors.append(23)
        n = n // 23
    while n % 29 == 0:
        factors.append(29)
        n = n // 29
    while n % 31 == 0:
        factors.append(31)
        n = n // 31
    factors = factors + [n]
    return factors
```