```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the same number of times in the factorization corresponding to how many times it is a factor. """
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(90)
    [3, 5, 7]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for num in range(3, int(n**0.5) + 1,while n % num == 0:
        factors.append(num)
        n = n // num
    return factors
```