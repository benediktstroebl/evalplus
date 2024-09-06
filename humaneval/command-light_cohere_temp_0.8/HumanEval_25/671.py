```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # initialize empty list
    factors = []
    # loop through 1 to n
    for i in range(1, n+1):
        # leave only primes in iter(1, n)
        if i % 2 == 0 or i == 1:
            continue
        else:
            # break loop if i is a prime number
            factors.append(i)
   
    return(factors)
```
The function will return a list of prime factors in the order of their occurrence in factorization.