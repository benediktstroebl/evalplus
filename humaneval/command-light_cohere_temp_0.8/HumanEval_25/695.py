```python
from typing import List
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        is_prime = True
        for i in range(3, int(n**0.5) + 1, stepby):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(i)
        n = n // i
    return factors
```