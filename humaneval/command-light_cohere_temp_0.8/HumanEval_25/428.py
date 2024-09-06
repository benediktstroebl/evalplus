```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factors = factorize(8)
    [2, 2, 2]
    >>> factors = factorize(25)
    [5, 5]
    >>> factors = factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(n)
    factors.append(2)  # if n % 4 == 0 else n // 2)
    factors.append(n)
    # Check for other odd factors
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
    return factors
```