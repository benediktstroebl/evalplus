```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # python 3 style factorization
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    elif n % 3 == 0:
            factors.append(3)
            n //= 3
    elif n % 5 == 0:
        factors.append(5)
        n //= 5
    elif n % 7 == 0:
        factors.append(7)
        n //= 7
    else:
        n = n // 3
        factors.append(list([3]*n))
    return factors
```