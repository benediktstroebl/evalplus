```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be number of times in the factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    []
    >>> factorize(16)
    []
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
    for x in factors:
        if x <= 1:
            factors.append(xx x)
        else:
            factors.append(x x* 1)
    return factors
```