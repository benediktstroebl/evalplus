```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```

This function, factorize, calculates the list of prime factors of a given number n, following the algorithm you provided. The function first checks for the divisibility by 2, adding it to the list of factors if the number is divisible by 2. It then checks for divisibility by numbers starting from 3 up to the square root of the number, adding each prime factor to the list as the number becomes divisible by it.