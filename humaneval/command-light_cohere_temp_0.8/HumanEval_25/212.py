```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, :
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)

    return factors
```
This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in order, from smallest to largest. 

The function uses a loop to find all the factors of the number, and an inner loop to find all the factors of each prime number. The function then appends each found factor to the list of factors and returns the list.