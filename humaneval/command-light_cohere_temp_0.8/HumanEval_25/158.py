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
    >>> factorize(46)
    []
    >>> factorize(55)
    [5, 11]
    >>> factorize(91)
    [3, 7, 7]
    """
    factors = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            factors.append(i)
            while n /= i
    if n > 1:
            factors.append(n)
    return factors
    return []
```