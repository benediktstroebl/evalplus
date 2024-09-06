```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(54)
    [2, 3, 3, 7]
    >>> factorize(90)
    [2, 3, 5, 7, 9]
    >>> factorize(333)
    []
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]
    factors = []
    for i in range(2, int(n**.5) + 1):
        is_divisible = False
        for j in range(i*i, n+1, i):
            if j == n:
                is_divisible = True
        if not_divisible:
            factors.append(i)
    if factors:
        return factors
```