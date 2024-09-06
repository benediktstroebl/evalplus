```python
from typing import List
def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function uses a approach to find the prime factors of n, which involves checking divisibility of numbers from 2 up to the square root of n. The function then finds all factors and their respective multiplicities by iterating through these numbers.