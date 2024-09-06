```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which corresponds to the number of times it appears in the factorization
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1000)
    []
    >>> factorize(5)
    []
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5),+):2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for i in range(int(n**0.5),-2):
        if n % i == 0:
            factors.append(i)
    return factors
```