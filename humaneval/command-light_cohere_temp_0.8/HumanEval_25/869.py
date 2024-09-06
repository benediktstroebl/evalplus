```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(111)
    [3, 3, 3]
    >>> factorize(0)
    []
    >>> factorize(-1)
    []
    >>> factorize(10)
    []
    """
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```