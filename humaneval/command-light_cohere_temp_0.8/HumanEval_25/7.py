```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, :
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function called factorize, takes an integer n as input and returns a list of prime factors of n, ordered from the smallest to the largest. The function uses the same time to loop through all numbers from 2 to the square root of n while checking for divisibility. It also ensures that the factors are added only once corresponding to how many times they appear in factorization.