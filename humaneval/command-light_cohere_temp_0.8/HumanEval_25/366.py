```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to the number it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(54)
    [2, 3, 3, 7]
    >>> factorize(3025)
    [5, 5, 5]
    >>> factorize(243)
    [3, 3, 3, 3]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [1]
    if n % 2 == 0:
        return [2]
    factors = []
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    return factors
```