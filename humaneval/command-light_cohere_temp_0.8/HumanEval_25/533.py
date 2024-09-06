```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2,  while n % i == 0 and i <= factors[-1]:
        factors.append(i)
        n = n // i
    factors.sort()
    important_order = [0] + sorted(factors)
    return important_order

# Example usage
n = 25
print(factorize(n))
```