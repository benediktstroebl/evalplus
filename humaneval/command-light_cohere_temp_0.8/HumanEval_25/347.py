```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is also listed number of times, which corresponds to how many times it appears in the factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(73)
    TraceError: 'int' object does not support item assignment
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```
This Python code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function first checks if `n` is less than or equal to 1, in which case it returns an empty list. Then, the function enters a loop, where it repeatedly divides `n` by its divisors (numbers that evenly divide `n`) until the next divisor doesn't make `n` a whole number anymore. The factors that are the numbers that were used to divide `n` and are therefore prime. 

The function then returns the list of prime factors of the original `n`, in order from smallest to largest, along with the number of times each factor appears in the factorization.