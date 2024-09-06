```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_factor = n % i == 0
        if is_factor:
            factors.append(i)
            while is_factor:
                n //= i
                is_factor = n % i == 0
                if is_factor:
                    factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
```

The factorization is done iteratively by checking successive integers starting from 2. The loop continues until the resulting quotient is 1, meaning that the number is completely factorized. To ensure that the list of factors is ordered from smallest to largest, it is appended to the list instead of inserted.