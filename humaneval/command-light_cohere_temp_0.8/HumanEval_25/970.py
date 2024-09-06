```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(30)
    [2, 3, 5]
    >>> factorize(100)
    []
    """
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while not n % i == 0:
            factors.append(i)
            n //= i
    if n == 1:
            return []
    return factors
```