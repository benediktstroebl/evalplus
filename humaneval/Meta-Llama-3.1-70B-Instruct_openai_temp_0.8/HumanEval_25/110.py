```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: The number to factorize
    :return: A list of prime factors
    """
    factors = []
    divisor = 2

    # find all factors
    while n > 1:
        # if n is divisible by divisor, it's a factor
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            # if divisor is not a factor, increment it
            divisor += 1

    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
print(factorize(100)) # [2, 2, 5, 5]
```