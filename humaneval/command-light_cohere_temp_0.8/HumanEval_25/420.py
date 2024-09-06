```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
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
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 2:
        if n % 3 == 0:
            factors.append(3)
        n //= 3
        elif n % 5 == 0:
            factors.append(5)
        n //= 5
        elif n % 7 == 0:
            factors.append(7)
        n //= 7
        else:
            # Continue checking higher primes
            # ...
        factors.append(n)
        return factors
    return factors
```