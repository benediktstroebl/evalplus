```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned in the order of their corresponding multiplications
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(46)
    []
    >>> factorize(47)
    [7]
    >>> factorize(300)
    [3, 3, 5, 7]
    """
    factors = []
    while n > 0:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
        else:
            m = n // 3
            factors.append([3, m, 3, 3])
            n = n // m
    return factors
```