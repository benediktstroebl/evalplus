```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [1]

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for d in range(3, int(n**0.5)+1, while n % d == 0:
        factors.append(d)
        n = n // d
    return factors
```