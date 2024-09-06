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
    factors.append(int(n))
    return factors
```
This function, factorize, takes an integer n as input and returns a list of its prime factors in order from smallest to largest. It uses a approach that starts with the assumption that all factors are even numbers and then checks for each prime factor until the square root of the number is reached. The function then returns a list of prime factors for n.