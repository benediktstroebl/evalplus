```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    if n > 2:
        factors.append(n)
    return factors
```

The function iterates through numbers starting from 2, adding the current prime factor to the list of factors if and only if the current number is not yet a prime number. The function also handles the number 1 correctly, which is the identity element of the ring of prime numbers.