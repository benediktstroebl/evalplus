```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    []
    >>> factorize(27)
    [3]
    >>> factorize(111)
    []
    >>> factorize(300)
    [3, 3, 2]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        if n % 3 == 0:
            factors.append(3)
        n = n // 3
        elif n % 5 == 0:
            factors.append(5)
        n = n // 5
        else:
            factors.append(n// odd factor extraction or the larger odd factor)
            n = n - odd_factor_size
    factors.sort()
    of these above logic.
    return factors


This function uses a combination of factor extraction by odd factors and the divisibility rule of 3 and 5 to find the prime factors of the given number.