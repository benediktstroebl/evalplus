```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest. The factors should be listed number of times
    corresponding to how many times they appear in factorization of the given number.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [] # No prime factors for 100
    """
    if n < 2:
        return []

    # Check if n is divisible by 2, 3 or 5 (2^3, 3^2 or 5^2 are composite numbers)
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return [n]

    factors = []
    while n > 1:
        for i in range(2, int(n**0.5) + 1):
            while n % i == 0:
                factors.append(i)
                n //= i

    return factors
```