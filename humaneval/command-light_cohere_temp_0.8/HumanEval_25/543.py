```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in factors:
        if i > 1:
            factors.append(i * i)
    return factors
```

This function goes through each prime factor of a given number and returns them in order of increasing size, starting from the smallest prime factor up to the largest one.