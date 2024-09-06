```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    """ if not n > 1: return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**.5) + 1, increment=4):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2: factors.append(n)
    return factors
```