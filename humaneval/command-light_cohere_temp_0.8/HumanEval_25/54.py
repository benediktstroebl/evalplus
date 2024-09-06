```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    If a list comprehension:
    a: i for i in range(2, n + 1) do 
        if n % i == 0: 
            yield i
    else: 
        continue
    """
    factors = []
    for i in range(2, n+1):
        if n % i == 0:  # if n is divisible by i, add i to factors list 
            factors.append(i)
            factors.append(i) # repeat i in factor list for every divisor
    return factors
```