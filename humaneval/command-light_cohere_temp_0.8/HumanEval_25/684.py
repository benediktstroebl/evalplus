```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    ```
    example usage:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(2)
    factors.append(n)
    for x in range(3, int(n**0.5) + 1):
        if n > 2 and n % x == 0:
            n = n / x
        factors.append(x)
    factors.append(x)
    return factors
```