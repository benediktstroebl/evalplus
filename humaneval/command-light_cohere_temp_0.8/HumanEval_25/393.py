```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the number of times it appears in the factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(77)
    [7, 7]
    >>> factorize(101)
    [3, 3, 5]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, :
        while n % i == 0:
            factors.append(i)
            n = n // i
    for i in range(int(n ** 0.5) + 1, :
        factors.append(i)
    return factors
```