```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization of the number
    Input number should be a power of two.
    >>> factorize(16)
    [4, 2]
    >>> factorize(64)
    [4, 2, 2, 2]
    >>> factorize(28)
    [2, 2, 7]
    >>> factorize(2)
    []
    >>> factorize(35)
    [3]
    """
    if n < 2:
        return []
    if n == 2:
        return [2]
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    for num in factors:
        if num > 1:
            factors.append(factors[num, num // num)
    return factors
```