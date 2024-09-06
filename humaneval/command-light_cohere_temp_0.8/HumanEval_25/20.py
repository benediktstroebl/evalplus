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
This function takes an integer n as input and returns a list of its prime factors in ascending order. It iterates through loop, continuously dividing by numbers until the input is a prime number or a number smaller than the square root of the input.