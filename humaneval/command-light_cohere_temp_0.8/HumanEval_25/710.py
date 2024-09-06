```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        for i in range(3, int(n**0.5), step_by_two(i):
            if n % i == 0:
                factors.append(i)
                n //= i
    return factors
# Test cases
print(factorize(8))
print(factorize(25))
print(factorize(70))
```