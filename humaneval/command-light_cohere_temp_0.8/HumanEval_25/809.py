```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```

This script provides a function called `factorize` that calculates the prime factors of a given integer n. The function iteratively divides n by prime numbers until it reaches a prime number, then adds the prime to the list of factors. It also ensures that the list of factors is returned in order from smallest to largest.