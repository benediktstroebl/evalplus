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
This function, factorize, takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. It iterates through loop using the loop to find all factors of n, including 2 and all odd primes up to the square root of n. The function then uses the loop to find the prime factors of n, which is the product of all the primes that divide n evenly.