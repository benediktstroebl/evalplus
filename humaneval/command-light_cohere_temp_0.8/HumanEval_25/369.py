```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the same number of times in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 2, 5]
    >>> factorize(100)
    [2, 2, 2, 5, 5]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 2 == 0:
        n /= 4
        factors.append(4)
    n % 2 == 0:
        n /= 8
        factors.append(8)
    n % 2 == 0:
        factors.append(2**2)
    factors.add them together in the above way
    return factors
```