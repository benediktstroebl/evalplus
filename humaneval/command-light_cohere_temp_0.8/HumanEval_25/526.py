```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times, which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors"""
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for num in factors:
        if num > 1:
            return [num] + factorize(num)
    return factors
```