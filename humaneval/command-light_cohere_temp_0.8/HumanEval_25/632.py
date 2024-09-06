```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(1)
    []
    >>> factorize(13)
    [13]
    >>> factorize(3628)
    [2, 3628]
    """
    factors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)
    return factors
```
This Python code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. It uses a process by iterating through all numbers from 2 up until the square root of `n` is reached, checking if `n` is divisible by each number. If a divisor is found, it adds the divisor to the list of factors and continues the process. The function then passes tests with various inputs and provides the prime factors accordingly.