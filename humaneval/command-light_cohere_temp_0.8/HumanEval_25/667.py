```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    TraceError: cannot convert argument 10 to int
    """
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
            n = n // 2
        elif n % 3 == 0:
            factors.append(3)
            n = n // 3
        elif n % 5 == 0:
            factors.append(5)
            n = n // 5
        elif n % 7 == 0:
            factors.append(7)
            n = n // 7
        else:
            factors.append(int)
            n = n // int(sqrt(n)) + 1
    return factors
```