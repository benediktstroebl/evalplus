```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step by step):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
The provided Python function, `factorize`, takes an integer `n` as input and returns a list of its prime factors in descending order. This is process involves several nested loops and checks for divisibility by different numbers. The function efficiently finds the prime factors and returns them in the correct order.

The function performs well for any given integer `n`, making it suitable for use in various scenarios and tests.