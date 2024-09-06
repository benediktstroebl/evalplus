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
    if n > 2:
        factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of its prime factors in order from smallest to largest. It uses a `while loop` to iterate through all the prime numbers, starting from 2 up, and `if` statement to check if `n` is divisible by `i`. If `n` is greater than 2, it adds `n` as the last prime factor.