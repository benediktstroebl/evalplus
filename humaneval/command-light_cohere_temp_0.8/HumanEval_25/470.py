```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5 / 2) + 1, :
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function `factorize()` takes an integer `n` as input and returns a list of its prime factors. The function works by first checking for the presence of odd factors and then iterates through the odd numbers to find the prime factors of the given number.