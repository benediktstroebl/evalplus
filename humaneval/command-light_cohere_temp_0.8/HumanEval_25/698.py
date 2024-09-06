```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, )):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function `factorize` in the provided code snippet computes the list of prime factors of a given integer `n`. It iteratively divides `n` by the smallest prime number that does not yet divide `n` evenly, and adds the corresponding prime to the list of factors.