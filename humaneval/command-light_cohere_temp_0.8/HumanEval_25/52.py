```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        m = int(n**.5)
        while m <= n:
            if n % m == 0:
                factors.append(m)
            n = n // m
    return factors
```