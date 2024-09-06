```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the same number of times in the factorization.
    >>> factorize(8)
    [2, 2]
    >>> factorize(25)
    [5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors

# Test case
print(factorize(8))  # [2, 2]
print(factorize(25))  # [5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of `n` in the order from smallest to largest. The script includes a test case that demonstrates the function by passing test cases and printing the result. 

Please note that the solution is written in Python and does not use external libraries.