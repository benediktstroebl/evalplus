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
    >>> factorize(100)
    [2, 2, 5, 5, 7]
    >>> factorize(255)
    [3, 3, 5, 7, 11]
    >>> factorize(32)
    []
    """
    factors = []
    while n % 2 == 0:
        n /= 2
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n /= i
        else:
            break
    if n > 2:
        factors.append(n)
    return factors
```