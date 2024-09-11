```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """

    # Initialize an empty list to store prime factors
    factors = []

    # Check for divisibility from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        # While i is divisible, add it to the list and divide n
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is a prime number greater than sqrt(n), add it to the list
    if n > 1:
        factors.append(n)

    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script works by continuously dividing the input number `n` by the smallest divisor `i` until it's no longer divisible. It does this by iterating from 2 to the square root of `n`, and for each divisor it finds, it adds it to the list of factors and divides `n` by it. If `n` itself is a prime number greater than the square root of `n`, it adds it to the list. The result is a list of prime factors of `n`, each appearing the number of times it appears in the factorization.