```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(77)
    [3, 3, 7]
    """
    factors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
        factors.append(i)
        n //= i
    for j in range(i+1, int(n**0.5)+1):
        while n % j == 0:
            factors.append(j)
        n //= j
    return factors
```