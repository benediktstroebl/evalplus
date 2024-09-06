```python
from typing import List
def factorize(n):
    factors = []
    while n > 1:
        i = 2
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```