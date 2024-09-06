```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(10000)
    [2, 2, 5, 5, 5, 5, 7, 11, 13, 17, 19]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while len(factors) > 1 and all(n % num for num in factors):
        factors.append(n)
        return factors
```
The code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function first checks if `n` is less than or equal to 1, and if so returns an empty list. Then, the function uses a while loop to factorize `n`. It checks for every divisor `d` of `n` (i.e. If `d  `d are the divisor of n` that all the numbers in `factors` divide `n`. Finally, the function returns the list of prime factors of `n` in order from smallest to largest.