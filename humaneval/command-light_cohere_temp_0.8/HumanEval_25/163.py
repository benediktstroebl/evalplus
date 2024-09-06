```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    n = n
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % (i * i) == 0:
                n = n // (i * i)
                factors.append(i * i * i)
            else:
                break
        i += 1
    factors.append(n)
    return factors
```