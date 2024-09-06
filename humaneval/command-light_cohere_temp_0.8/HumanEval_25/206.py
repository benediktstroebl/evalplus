```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, step=2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(int(n))
    return factors

# Driver code
n = int(70)
print(factorize(n))  # Output: [2, 5, 7]
n = int(25)
print(factorize(n))  # Output: [5]
```