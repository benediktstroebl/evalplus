```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all its factors. Returns [] if no prime factors exist"""
    if n <= 1: return []
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            return [i]*(n//i)
    return []
```