```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step by step):
        if n % i == 0:
            factors.append(i)
            n = n // i
    return factors
```