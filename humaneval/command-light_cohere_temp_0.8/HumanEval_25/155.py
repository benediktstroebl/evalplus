```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(59)
    [3, 3, 7]
    >>> factorize(53)
    [3, 3, 3, 7]
    >>> factorize(4623)
    [2, 2, 2, 2, 23]
    >>> factorize(777)
    [3, 3, 3, 37, 77]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 3 == 0 and factors.append(3)
        n % 5 == 0 and factors.append(5)
    n % 7 == 0 and factors.append(7)
    n % 11 == 0 and factors.append(11)
    n % 13 == 0 and factors.append(13)
    while n > 1:
        n = n // n
    return factors

``` 
Do you have any other questions related to Python or coding problems?