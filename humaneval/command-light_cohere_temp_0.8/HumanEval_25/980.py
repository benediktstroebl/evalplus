```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to the number of times it appears in factorization
    Input number should be equal to the product of all its factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    factors.append(n)
    if n >= 1 else factors.append(None)
    for i in range(3, int(n**0.5) //, n /= i, factors. if i % 2 == 1 else:
        break
    return factors
```