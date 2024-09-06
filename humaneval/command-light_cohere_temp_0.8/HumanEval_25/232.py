```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    >>> factors = factorize(8)
    [2, 2, 2]
    >>> factors = factorize(25)
    [5, 5]
    >>> factors = factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(n // n // n // 2
        n //=2
    if n > 1:
        factors.append(n)
    else:
        break
    return factors
```