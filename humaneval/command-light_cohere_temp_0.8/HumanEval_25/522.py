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
    factors.append(n)

    return factors
```
This function takes an integer n and returns a list of its prime factors. It does so by first checking for the smallest prime factor, 2 in the number and appends it to the factors list. It then checks for the prime factors starting from 3 up until the square root of the number is reached.

The function does not depend on any other function or variable.