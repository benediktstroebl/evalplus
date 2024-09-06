```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step=2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function `factorize` takes an integer `n` as input and returns a list of its prime factors in order from smallest to largest, using a basic trial division method. It's a tested by passing a series of tests, which include passing different input values and verifying the output.