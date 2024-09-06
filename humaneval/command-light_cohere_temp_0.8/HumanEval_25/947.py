```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which correspond to how many times it appears in factorization
    >>> factors25 = factorize(25)
    [5, 5]
    >>> factors48 = factorize(48)
    [2, 2, 3, 2, 7]
    >>> factors80 = factorize(80)
    [2, 2, 4, 2, 5, 2, 2, 8]
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
    for j in range(int(n**0.25), + 1):
        factors.append(j)
    return factors
```