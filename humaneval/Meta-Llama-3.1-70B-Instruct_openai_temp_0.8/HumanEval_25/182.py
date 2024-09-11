```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: Input integer
    :return: List of prime factors
    """
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors of `n`. The function works by dividing `n` by the smallest divisor (starting from 2) until it is no longer divisible. The divisor is then incremented and the process is repeated until `n` is reduced to 1. The list of divisors is returned as the result.

The test cases demonstrate the correctness of the function.