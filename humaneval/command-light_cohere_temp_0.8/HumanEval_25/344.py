```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(97)
    [3, 3, 7]
    >>> factorize(111111)
    [7, 11, 11]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    while n % 3 == 0:
        n /= 3
        factors.append(3)
    while n % 5 == 0:
        n /= 5
        factors.append(5)
    while n % 7 == 0:
        n /= 7
        factors.append(7)
    while n % 11 == 0:
        n /= 11
        factors.append(11)
    n = 1
    return factors
```