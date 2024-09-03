```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed in order of how many times they appear in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(9)
    []
    """
    if n <= 1:
        return []
    # Remember prime factors are always odd
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 4 == 0:
        factors.append(3)
        n //= 4
    while n % 8 == 0:
        factors.append(5)
        n //= 8
    while n % 16 == 0:
        factors.append(7)
        n //= 16
    while n % 32 == 0:
        factors.append(13)
        n //= 32
    while n % 128 == 0:
        factors.append(191)
        n //= 128
    factors.append(n)
    return factors
```