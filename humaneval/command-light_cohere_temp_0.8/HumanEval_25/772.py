```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(49)
    []
    >>> factorize(49)
    [7]
    >>> factorize(100)
    [2, 2, 5, 5, 7]
    """

    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    while n != 1:
        factors.append(int(n % 3))
        n = n // int(n % 3)

    if n > 1:
        factors.append(n)
    return factors

```