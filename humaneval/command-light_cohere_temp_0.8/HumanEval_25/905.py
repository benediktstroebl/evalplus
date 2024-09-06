```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(0)
    []
    >>> factorize(-8)
    []
    >>> factorize(16)
    [2, 4]
    >>> factorize(52)
    [2, 13]
    >>> factorize(1000)
    [2, 3, 5, 25, 8, 70, 100]
    """
    # sort factors and get length of longest
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
            n /= 2
        elif n % 3 == 0:
            factors.append(3)
            n /= 3
        else:
            factors.append(5)
            n /= 5
    factors.append(7)
    factors.reverse()
    factor list

    return factors
```