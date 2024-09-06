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
    factors.append(n)
    return factors
```
The function `factorize` takes an integer `n` as input and returns a list of its prime factors. It uses a process to find the prime factors of `n`, which involves dividing `n` by the smallest prime factors until `n` is no longer divisible by any smaller prime number. The result is a list of the prime factors, listed in order from smallest to largest.