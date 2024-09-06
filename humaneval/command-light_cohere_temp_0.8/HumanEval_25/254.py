```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    If number <= 1, return [0]
    If number is even, return []
    If number < 2, return [2]
    If number > 2, return [2, 2]
    If n is divisible by 2 or 3, return [2, 2]
    If n is divisible by larger integer within range [3, n-1], return factorize(n/int)
    If n is prime, return [n]
    If n = a*b and a and b are prime, return [a, b]
    """
    if n <= 1:
        return [0]
    elif n % 2 == 0:
        return []
    elif n < 2:
        return [2]
    elif n > 2:
        return [2, 2]
    elif n % 3 == 0:
        return [2, 2]
    elif n % 5 == 0:
        return [0]
    elif n % 7 == 0:
        return [0]
    elif n % 11 == 0:
        return [0]
    elif n % 13 == 0:
        return [0]
    elif n % 17 == 0:
        return [0]
    elif n % 31 == 0:
        return [0]
    elif n % 61 == 0:
        return [0]
    elif n % 103 == 0:
        return [0]
    elif n % 167 == 0:
        return [0]

    if n >= 17:
        prime_factors = []
        for p in range(2, int(n**0.5) + 1):
            while n %= p == 0:
                prime_factors.append(p)
                n = n // p
        if len(prime_factors) > 1:
            return prime_factors
    else:
        return [0]
```