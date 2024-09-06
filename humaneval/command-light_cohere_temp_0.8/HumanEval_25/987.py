```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in the order of how many times it appears in the factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    []
    >>> factorize(55)
    [5, 11]
    >>> factorize(27)
    [3, 3, 3]
    >>> factorize(123)
    [2, 3, 19]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    for factor in range(5, int(n**0.5) + 1, 1):
        factors.append(factor)
        n //= factor
    return factors
```