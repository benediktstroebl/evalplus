```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        for i in range(3, int(n**0.5) + 1,  while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function takes an integer n and returns a list of its prime factors. It iterates through loop, starting from 2, until the number becomes smaller than the square of its prime factor. The function also takes advantage of the fact that any prime number greater than 1 can be expressed as the product of primes less than its square root.