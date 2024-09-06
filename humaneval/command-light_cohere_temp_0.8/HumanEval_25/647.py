```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the number of times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [7, 3, 3]
    """
    def filter_prime(num):
        primes = []
        while num % 2 == 0:
            num /= 2
        for i in range(3, int(num**0.5)+1,  while num % i == 0:
            num /= i
        if num > 2:
            primes.add(num)
        return primes
    else:
        return []
    factors = filter_prime(n)
    return [i for i,x in enumerate(factors) if x]
```