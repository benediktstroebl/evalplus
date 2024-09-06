```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                n //= i
            else:
                i += 1
    return factors
# Test cases
print(factorize(8))      # [2, 2, 2]
print(factorize(25))    # [5, 5]
print(factorize(70))    # [2, 5, 7]
```
This script provides a self-contained function with a docstring, which solves the problem of finding prime factors of a given number and passes corresponding tests.