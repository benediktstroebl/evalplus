```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for divisor in range(2, n):
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                n //= divisor
                count += 1
            if count > 0:
                factors.append(divisor)
                factors.extend([divisor] * count)
    if n > 1: 
        factors.append(n)
    return factors
```
The factorization algorithm works by dividing the number gradually by each potential divisor from 2 up to the number itself (n) last. The algorithm detects how many times each factor appears in the number and incorporates it into the final list. The resulting list includes every prime factor, presented however many times it appears as the factor in the number restoration.