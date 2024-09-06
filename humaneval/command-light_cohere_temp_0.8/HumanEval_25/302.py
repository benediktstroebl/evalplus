```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization
    Input number should be a product of its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    []
    >>> factorize(6)
    []
    >>> factorize(1)
    []
    """
    if n <= 1:
        return []
    else:
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        while n > 1:
            if n % 3 == 0 or n % 5 == 0:
                factors.append(n // 2)
            n = n // 5
            elif n % 7 == 0:
                factors.append(3)
            n = n // 7
            else:
                factors.append(int(n))
                n = n // int(n, prime=2)
        return factors
```