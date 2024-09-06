```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    Keep track of factors and counter.
    factors = []
    set()
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
            if len(factors) == i:
                break
    counter = 0
    factors.append(counter)
    counter += 1
    return factors
```