```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If number is the product of all factors"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This Python function, `factorize`, takes an integer `n` as input and returns a list of its prime factors in descending order. It uses a algorithm that first finds the smallest factor by repeatedly dividing by 2, and then finds subsequent prime factors by using the fact that a factor `i` is itself a prime factor for `n/i`. The function ensures that the prime factors are listed in the correct order, with the smallest factor first and the largest factor last.