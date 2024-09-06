```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 4 == 0:
        factors.append(4)
        n //= 4
    while n % 8 == 0:
        factors.append(8)
        n //= 8
    for factor in factors:
        while n % factor == 0:
            n //= factor
    factors.append(n)
    return factors
```