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
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
The function factorizes a given integer n and returns a list of its prime factors in ascending order. It starts by checking for divisibility with 2 and adds 2 to the list of factors until n is not divisible by 2. Then, starting from 3, it checks for divisibility with consecutive square numbers until the square root of n is less than n.