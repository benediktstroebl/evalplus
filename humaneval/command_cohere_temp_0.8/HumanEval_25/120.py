```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor and i != n // i:
            factors.append(i)
            while is_factor:
                n //= i
                is_factor = n % i == 0
                if is_factor and i != n // i:
                    factors.append(i)
        elif n > 1:
            factors.append(n)
    return factors
```