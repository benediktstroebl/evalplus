```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization of the number.
    """ Example factor 2 for the prime numbers, i. prime numbers, except for odd numbers"""
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % (i*i) == 0:
                n //= (i*i)
                factors.append(i)
                n = n // (i * i)
            i += 2
    if n > 2:
        factors.append(n)
    return factors
```