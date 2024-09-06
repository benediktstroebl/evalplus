```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    []
    >>> factorize(9)
    []
    """
    if n <= 1:
        return []
    
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
```