```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1)
    []
    >>> factorize(10)
    [2, 5]
    >>> factorize(55)
    [5, 11]
    >>> factorize(666)
    [2, 3, 37, 6, 66]
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n // 2
    while n % 3 == 0:
        factors.append(3)
        n // 3
    for i in range(5, int(n ** 0.5) // 1, 2, 4:
        factors.append(i)
        n // i

    return factors
```