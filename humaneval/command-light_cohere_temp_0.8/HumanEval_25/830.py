```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all the factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(160)
    [] # not a prime number
    >>> factorize(16)
    [2, 2]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                n //= i
    factors.sort()
    prime_factors = []
    for i in range(len(factors)):
        prime_factors.append(factors[i] * factors[i])
    return prime_factors
``` 
This script provides a function that, given an integer n, returns a list of its prime factors in order of magnitude, from smallest to largest.