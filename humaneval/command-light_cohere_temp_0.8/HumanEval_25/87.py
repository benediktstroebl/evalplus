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
    >>> factorize(16)
    [2, 2, 2, 2]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 5, 5]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)

    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % (i * i) == 0:
                n /= (i * i)
            factors.append(i)
        i += 1

    for num in factors:
        if num > 1:
            factors.append(num * factors[num])

    return factors
```