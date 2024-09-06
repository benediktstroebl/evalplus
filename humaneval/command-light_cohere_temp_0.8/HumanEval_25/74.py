```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be a product of all its factors. Returns empty list if input is not a prime."""
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**.5) + 1, by=2):
        while n % i == 0:
            factors.append(i)
        n = n // i
    if n > 2:
        factors.append(n)
    return factors
```