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
    if n > 2:
        factors.append(n)
    return factors
```
This code provides a solution for the given problem, which is to return the list of prime factors of a given integer n in order from smallest to largest. 

Note that the function does not accept negative numbers and only returns positive integers.