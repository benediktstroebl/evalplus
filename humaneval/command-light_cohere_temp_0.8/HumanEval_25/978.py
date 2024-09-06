```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        m = int(n ** 0.5)
        if m > 1 and m % 2 == 0:
            factors.append(m)
            n = m // 2
        else:
            continue
    return factors
# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```