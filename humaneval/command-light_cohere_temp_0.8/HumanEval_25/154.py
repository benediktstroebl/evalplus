```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, ]:
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(int(n))
    return factors
```
The function identifies the prime factors of a given number by iterating up to the square root of the number and checking for divisibility. It also handles the manual checking for divisibility and factoring by individual prime numbers, ensuring that the list of prime factors is returned in order from smallest to largest.