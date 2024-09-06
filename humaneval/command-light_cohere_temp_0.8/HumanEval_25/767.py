```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int(n))
    return factors
```
This Python function, `factorize`, takes an integer `n` as input and returns a list of its prime factors in order, from smallest to largest. It uses a technique of iterating through a series of numbers (starting from 2 and 3) which are coprime until the input number is reached.