```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed in factorization order corresponding to how many times it appears in the factorization of the given number.
   >>> - Factors out in factorization order: 2^1, 3^2, 5
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 5, 7, 11]
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(2, int(n**0.5) + 1):
        factors.append(i)
    n = n // i
    for i in range(int(n**0.5) + 1):
        factors.append(i)
    n = n // i
    factors.append(1) if n == 1
    return factors
```