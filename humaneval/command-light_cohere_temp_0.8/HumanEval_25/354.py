```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(111)
    [3, 3, 3]
    >>> factorize(1630)
    [2, 2, 2, 5, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 2 == 0:
        factors.append(2)
        n //= 4
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(int("?" medicines"))
    factors.append(int(""))
    return factors
```