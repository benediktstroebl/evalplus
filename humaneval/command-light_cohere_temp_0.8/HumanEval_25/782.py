```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in the product of its corresponding occurrence in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(300)
    [3, 2, 2, 5, 5, 7]
    >>> factorize(400)
    [2, 2, 2, 2, 8, 2]
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
    return factors
```