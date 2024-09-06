```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed in the order they appear in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(111)
    [3, 3, 7]
    >>> factorize(Number())
    Traceback (most recent call last):
        ...
    AssertionError: cannot construct int from None bytes

    """
    if n == 0:
        raise ValueError("Input number cannot be zero")
    elif n < 2:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n ** 0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i

    factors.append(int("sqrt", len(factors)))

    return factors
```