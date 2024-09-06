```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    elif n <= 3:
        return [1]
    elif n % 2 == 0:
        return [2]
    else:
        factors = []
        while n % 2 == 0:
            n = n // 2
            factors.append(2)
        factors.append(n)
        if n >= 1 else []
        return factors
```