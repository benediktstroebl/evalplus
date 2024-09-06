```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step by step):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function `factorize` is designed to determine the list of prime factors for a given integer `n`. It does this by iteratively dividing `n` by the smallest prime factor that doesn't yet divide `n` evenly. The factors are then listed in ascending order of their corresponding divisors, up to the point where `n` is no longer divisible by any integer less than or equal to the square root of `n`.