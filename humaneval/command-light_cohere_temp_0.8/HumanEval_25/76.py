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
    >>> factorize(53)
    [3, 3, 7]
    >>> factorize(3838)
    [2, 2, 2, 5, 7]
    >>> factorize(93)
    [3, 3, 3, 7]
    """
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            n //= i
            if n == 1:
                break
    for j in range(i + 1, int(n**0.5) + 1):
        if n % j == 0:
            factors.append(j)
            n //= j
            if n == 1:
                break
    return factors
```