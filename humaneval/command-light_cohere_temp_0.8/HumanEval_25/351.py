```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, i += 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function first checks for the factor of 2 and appends it to the list. Then it checks for the prime factors starting from 3 up up to the square root of the input number and keeps adding them to the list until they are not divisible by any of those prime factors.