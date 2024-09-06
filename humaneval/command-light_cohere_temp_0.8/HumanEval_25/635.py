```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    If the number is 1, return [0] for consistent empty list
    """
    if n == 1:
        return [0]
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2, while n % i == 0 and i <= √(n):
        factors.append(i)
        n = n // i
    for i in range(5, len(factors) + 1, -1):
        factors.append(i ** if i == factors[i-1] else None
    return factors
```