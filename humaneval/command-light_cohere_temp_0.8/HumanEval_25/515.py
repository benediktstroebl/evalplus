```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If factorize(8)
    > [2, 2, 2]
    factorize(25)
    > [5, 5]
    factorize(70)
    > [2, 5, 7]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    factors.append(n // 1)
    for x in range(3, int(n**0.5) + 1):
        if n % x == 0:
            factors.append(x
    factors.append(x
    x)
    factors.append(1)
    return factors
```
The function returns a list of prime factors of the given number n in the order of their occurrence in factorization.