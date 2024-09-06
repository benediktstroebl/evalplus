```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5 / 2, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function, factorize, accepts an integer n and returns a list of its prime factors in order from smallest to largest. The function utilizes the approach to find the prime factors by dividing the number by the smallest prime factor until it is no divisible. It then iterates through the smaller prime factors until it gets a factor that is not a prime, in which case, it starts again from the next prime number.