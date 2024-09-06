```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If the factors are those numbers that are divisible by 2 or 5 only
    2 <= n < 5
    if n <= 2:
        return [2]
    elif n % 2 == 0:
        return [2, n // 2]
    elif n % 3 == 0:
        return [3]
    elif n % 5 == 0:
        return [5]
    for i in range(6, n // 2 + 1, 2):
        if n % i == 0:
            return [i, n // i] + [i] + [n // (i * i)]
    return []
```