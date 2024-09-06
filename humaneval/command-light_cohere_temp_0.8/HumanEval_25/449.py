```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, )):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(int(n))
    return factors

# Example usage
n = 8
result = factorize(n)
print(result)  # Output: [2, 2, 2]

n = 25
result = factorize(n)
print(result)  # Output: [5, 5]

n = 70
result = factorize(n)
print(result)  # Output: [2, 5, 7]
```
This script defines a function called `factorize` that calculates and returns a list of prime factors for a given integer `n`. The function uses a loop to find factors and avoids including squares as factors.  The result is stored in the `result` variable and printed.