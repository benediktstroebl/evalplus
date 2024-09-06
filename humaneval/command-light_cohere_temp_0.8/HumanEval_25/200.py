```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned in the order of the factorization, i.
    # Find the prime factors
    For example, 35 = 5 x 7, so it will return [5, 7]
    # Do the same for all factors of n
    factors = []
    for i in range(1, int(n**0.5) + 1):
        factors = []
        while n % i == 0:
            factors.append(i)
            n = n // i
        factors.append(n)
        return factors
    return factors
```