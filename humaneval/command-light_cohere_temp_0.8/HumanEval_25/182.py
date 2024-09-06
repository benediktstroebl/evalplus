```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2, n % i == 0:
        factors.append(i)
    n = n // i
    factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of prime factors of n, in order from smallest to largest, using a strategy that first finds factors of 2, then 3, 4, and so on, using the Extended Euclidean Algorithm.