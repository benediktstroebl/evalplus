```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```

This function, `factorize`, uses a loop to find the prime factors of a given number. It adds the factors of the number to the `factors` list as long as the number is not divisible by the corresponding prime.