```python
from typing import List
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]

    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
   
    while n > 1:
        for d in range(3, int(n**.5) + 1, 2):
            if n % d == 0:
                n //= d
                factors.append(d)
    return factors
```