```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in the order of their corresponding multiplicity in the factorization of n.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(81)
    [3, 3, 7]
    >>> factorize(97)
    [3, 3, 7, 11]
    >>> factorize(106)
    [2, 3, 5, 6]
    >>> factorize(3628)
    [2, 2, 2, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        for i in range(3, int(n**0.5) + 1, while n % i == 0:
            factors.append(i)
            n //= i

    return factors
```