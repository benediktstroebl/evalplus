```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times, which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(105)
    [3, 5, 5]
    >>> factorize(16)
    []
    """
    if n <= 1:
        return []

    d = 1
    while d * d <= n:
        if n % d == 0:
            factors = [d]
            while n % d == 0:
                n //= d
                factors.append(d)
            d += 1
        else:
            break

    if n > 1:
        factors.append(n)

    return factors
```