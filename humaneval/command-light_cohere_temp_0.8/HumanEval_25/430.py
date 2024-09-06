```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        if n % 3 == 0:
            factors.append(3)
        n = n // 3
        elif n % 5 == 0:
            factors.append(5)
        n = n // 5
        elif n % 7 == 0:
            factors.append(7)
        n = n // 7
    else:
        factors.append(int)
    return factors
```