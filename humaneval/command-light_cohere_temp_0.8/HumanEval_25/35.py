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
    if n > 2:
        factors.append(n)
    return factors
```
This code defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. It uses a list comprehension and the `while` loop to find the prime factors of `n` in the correct order, from smallest to largest. This function is a result and is self-contained, as it does not rely on any other functions or modules.