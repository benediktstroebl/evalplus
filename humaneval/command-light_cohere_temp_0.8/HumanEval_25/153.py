```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(82)
    [] # Not a prime number
    >>> factorize(27)
    [3] # Not a prime number
    """
    factors = []
    while n > 1:
        is_prime = False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = True
                n = n / i
        if is_prime:
            factors.append(i)

    return factors
```