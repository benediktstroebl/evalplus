```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**.5) + 1, by=2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors
```
This function uses a simple algorithm to find the prime factors of a given number. It starts by checking for the factor 2, and then iterates through the other prime factors up to the square root of the number.