```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(49)
    [7, 3, 7]
    >>> factorize(101)
    [3, 7, 101]
    >>> factorize(101)
    [2, 51, 101]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 2
    while n > 1:
        if n % 3 == 0:
            n /= 3
        else:
            factors.append(n)
    n // 3
    for x in factors:
        x = int(x)
        factors.append(x x * int(x))
    return factors
```