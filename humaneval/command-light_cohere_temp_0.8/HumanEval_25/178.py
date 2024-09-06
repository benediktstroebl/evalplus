```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    A prime factor is a whole number that can only be divided by itself and 1.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(49)
    [7]
    >>> factorize(59)
    Trace underside error
    """
    if n <= 1:
        return []
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
    for num in factors:
        if num > 1:
            factors.append(factors[num]
    return factors
``` 
This code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function first checks if `n` is less than or equal to 1, and if so returns an empty list. It then iterates through a the numbers 2, 3, 4, and 5 (which are the prime factors of 2) until `n` is not divisible by any of these numbers. The function then starts iterating from 3, and checks if `n` is divisible by the square of `i`. If `n` is not divisible by `i`, the function appends `i` to the list of prime factors and then divides `n` by `i`. The function then starts iterating from 2 again until the square of `i` is less than `n`, and appends `i` to the list of prime factors.