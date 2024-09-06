```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Input number:
    """
    Factors:
    1 -> 2
    2
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i <= n // 2:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    for j in factors:
        if j != 2:
            factors.append(factors[j] * factors[j]
    return factors
```