```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step = i*2:
        while n % step == 0:
            factors.append(step)
            n = n // step
    factors.append(n)
    return factors
```

This function, `factorize`, accepts an integer `n` as input and returns a list of its prime factors. It uses a `while loop` to discover the factors of the number, starting with the factors 2 and 3, and it utilizes a nested `while loop` to locate the prime factors of bigger numbers. The final result is a list of prime factors of the original number, listed in ascending order.