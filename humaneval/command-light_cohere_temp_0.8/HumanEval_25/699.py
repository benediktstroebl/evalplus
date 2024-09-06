```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(170)
    [2, 17, 17]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    while n % 3 == 0:
        n /= 3
    for i in range(5, int(n**0.5), n // 5):
        factors.append(i)
    n = 1
    for i in factors:
        while n % i == 0:
            n /= i
    return factors
```