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
    >>> factorize(59)
    []
    >>> factorize(19)
    [19]
    """
    factors = []
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
        factors.append(i)
        factors.append(n//
        factors
    factors.sort()
    prime_factors = []
    for factor in factors:
        prime_factors.append(factor*factors.count(factor))
        prime_factors
    return prime_factors
```