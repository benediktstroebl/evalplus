```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []

    d = [1]
    for i in range(2, int(n**0.5) + 1):
        while d[-1] * d[-1] <= n:
        while n % i == 0:
            n //= i
            d.append(i)

    return d
```
This function, `factorize`, takes an integer `n` as input and returns a list of its prime factors in order of magnitude, from smallest to largest. The function works by iteratively generating divisors from 2 up until the current divisor does not leave any remainder when divided by itself. It keeps track of the factors in a list `d` at each step. 

Finally, it returns the list `d` which contains all the prime factors.