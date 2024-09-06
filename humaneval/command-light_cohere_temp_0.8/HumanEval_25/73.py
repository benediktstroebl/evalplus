```python
from typing import List
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        for d in range(2, int(n**0.5) + 1):
            if n % d == 0:
                factors.append(d)
                n = n // d
    return factors
# Example usage:
print(factorize(8))
print(factorize(25))
print(factorize(70))
```