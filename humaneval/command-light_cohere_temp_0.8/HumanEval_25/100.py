```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the number of times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(111)
    [3, 3, 3, 1]
    >>> factorize(666)
    [2, 2, 3, 3, 6, 6]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in factors:
        if j > 1:
            factors.append(j*j)
    return factors
```