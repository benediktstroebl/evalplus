```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        for i in range(3, int(n**0.5) + 1, :
            if n % i == 0:
                factors.append(i)
                n = n // i
        factors.append(n)
    return factors
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a algorithm to find the prime factors of `n`, which involves repeatedly dividing `n` by its smallest prime factor until the factor becomes larger than the square root of `n`.  The function then returns a list of the found prime factors, in order from smallest to largest.