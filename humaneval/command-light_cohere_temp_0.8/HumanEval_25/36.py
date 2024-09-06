```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which corresponds to the factor's position in factorization
    Input number should be equal to the product of all the factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(53)
    []
    >>> factorize(12)
    []
    """
    factors = []
    while n % 2 == 0:
        n /= 2
    for i in range(3, int(n**0.5), inclusive):
        while n % i == 0:
        factors.append(i)
        n /= i
    return factors
```