```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    >>> factors = factorize(8)
    [2, 2, 2]
    >>> factors = factorize(25)
    [5, 5]
    >>> factors = factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % (i + 2) == 0:
                n /= (i + 2)
            else:
                break
        i += 2
    factors.add((i = n)
    return factors
```
Do you require any other assistance related to Python scripts or code quality?