```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, )):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(int(n))
    return factors
```
The function factorize in this code takes an integer n as input and returns a list of its prime factors in order from smallest to largest. The function uses the same method as before with smaller primes, but also adds the remaining prime factor (which is larger than all the smaller primes) at the end of the list.