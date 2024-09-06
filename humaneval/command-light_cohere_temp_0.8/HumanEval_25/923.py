```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7]
    >>> factorize(101)
    [2, 3, 5, 101]
    >>> factorize(102)
    [2, 2, 101]
    >>> factorize(107)
    [7]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 7 == 0:
        factors.append(7)
        n //= 7
    for i in range(3, int(n**(1) // 3) + 1, 2):
        if n % i == 0:
            factors.append(i)
        n //= i
    return factors
```