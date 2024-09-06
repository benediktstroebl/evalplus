```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    We use a factors in the order of fact, so we can make use of the 'isprime' function.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(16)
    [2, 2, 2, 2]
    >>> factorize(55)
    [5, 11]
    >>> factorize(3096)
    []
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 3 == 0:
        n /= 3
    for i in range(5, int(n ** 0.5) + 1, :
        factors.append(i)
    n % i == 0:
        n /= i
    return factors
```