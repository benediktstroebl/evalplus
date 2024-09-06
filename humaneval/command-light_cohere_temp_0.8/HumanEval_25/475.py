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
    if n > 2:
        factors.append(n)
    return factors
```
This code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a method of trial and error, iterating through the factors of the number and checking if they divide evenly into the original number.