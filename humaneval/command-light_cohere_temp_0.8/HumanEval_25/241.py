```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    if not n:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**.5) + 1, by = 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This code defines a function factorize that takes an integer n as input and returns a list of its prime factors. The function first checks if n is 0 and returns an empty list if so. Then, it initializes an list called factors to store the prime factors. Then, it starts a loop while n is odd, and inside the loop, it adds the current prime factor to the factors list. Additionally, it divides n by the current prime factor and continues this process until it finds a prime factor of n.