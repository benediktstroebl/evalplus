```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    []
    >>> factorize(60)
    []
    >>> factorize(91)
    [3, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 3 == 0 and factors.append(3)
    n % 5 == 0 and factors.append(5)
    n % 7 == 0 and factors.append(7)
    while n != 1:
        return factors

``` 
Do you need help with anything else?