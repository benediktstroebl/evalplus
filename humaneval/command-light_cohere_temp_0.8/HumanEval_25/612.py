```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n //= i
    for j in factors:
        factors.append(j)
    return factors
```
Do you need help with anything else?