```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(3629)
    [2, 2, 2, 3, 6, 9]
    >>> factorize(418)
    [2, 3, 6, 9]
    >>> factorize(14421)
    [3, 2, 2, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        if n % 3 == 0:
            factors.append(3)
        n //= 3
        elif n % 5 == 0:
            factors.append(5)
        n //= 5
        elif n % 7 == 0:
            factors.append(7)
        n //= 7
        else:
            factors.append(int)
        n = n // 7
    return factors
```