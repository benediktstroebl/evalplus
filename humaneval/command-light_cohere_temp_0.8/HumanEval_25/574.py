```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5 / 2, step by step):
        if n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of its prime factors in descending order. It iterates through a process starting from small primes and checks if n is divisible by it. Then, it adds the prime to the list of factors and divides n by that prime to continue this process until n is no longer divisible by 2 or smaller prime numbers.