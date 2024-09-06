```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in the factorization of the number.
    >>> [2]  # 2s
    >>> [2] + [2, 2]
    >>> [3] + [3, 3]
    >>> [2, 4, 8, 16] + [16, 8, 4, 2]
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(36)
    [2, 2, 6]
    >>> factorize(600)
    [2, 3, 2, 2, 3, 2]
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 3 == 0 and factors.append(3)
        n % 5 == 0 and factors.append(5)
    n % 7 == 0 and factors.append(7)
    n % 11 == 0 and factors.append(11)
    n % 13 == 0 and factors.append(13)
    n % 17 == 0 and factors.append(17)
    n % 19 == 0 and factors.append(19)
    n % 23 == 0 and factors.append(23)
    n % 29 == 0 and factors.append(29)
    n % 31 == 0 and factors.append(31)
    n % 37 == 0 and factors.append(37)
    n % 41 == 0 and factors.append(41)
    n % 43 == 0 and factors.append(43)
    else:
        factors.append(n)
    return factors
```