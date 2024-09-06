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
The factorization algorithm works by iteratively dividing the number by the smallest possible divisors from 2 to the number itself. When a divisor is found, it is added to the list of factors, and the count of how many times it appears is recorded. The process continues until the number is reduced to 1, at which point the final list of factors is returned in ascending order.