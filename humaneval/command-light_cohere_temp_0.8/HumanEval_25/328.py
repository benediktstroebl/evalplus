```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeases in factorization.
    Input number should be equal to the product of all factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(76)
    [] # not a prime number
    >>> factorize(120)
    [] # not a prime number
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n // 2
    while n % 4 == 0:
        factors.append(4)
        n // 4
    while n % 8 == 0:
        factors.append(8)
        n // 8
    while n % 16 == 0:
        factors.append(16)
        n // 16
    while n % 32 == 0:
        factors.append(32)
        n // 32
    while n % 64 == 0:
        factors.append(64)
        n // 64
    while n % 128 == 0:
        factors.append(128)
        n // 128
    factors.reverse()
    factored_iter = iter(factors)
    return list(factored_iter)
```