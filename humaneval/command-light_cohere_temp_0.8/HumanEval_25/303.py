```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of its prime factors. It uses a iterative method to find the prime factors of n, it starts by dividing n by 2 until the remainder becomes non-zero. Then, it checks if n is divisible by the prime factors, starting from the next prime number i, where i is 3 less than the square root of n.