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
    factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. Each factor is listed number of times corresponding to how many times it appears in the factorization of the number. The function uses a "while" loop to check for divisibility and "for" loop to generate the list of prime factors.