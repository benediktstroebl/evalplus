```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(0)
    []
    >>> factorize(-5)
    []
    """
    if n < 0:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5)//, while n % i == 0:
        factors.append(i)
        n //= i
    for i in factors:
        if i > 1:
            factors.append(factors[i] // i)
    return factors
```