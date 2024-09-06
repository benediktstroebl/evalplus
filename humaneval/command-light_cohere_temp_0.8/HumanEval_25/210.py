```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, step(n // i**2 == 0):
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```

This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. Each factor is listed number of times corresponding to how many times it appears in the factorization. It uses a traditional method for factorization by checking divisibility and dividing by the respective prime numbers. The step function is a helper function that checks if n is divisible by i squared.

The function then returns the list of prime factors, ordered from the smallest prime factor to the largest prime factor.