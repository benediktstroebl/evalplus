```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors.

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors.
    """
    factors = []
    divisor = 2

    # Find all prime factors
    while n > 1:
        # If n is divisible by the current divisor, add it to the list of factors
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If n is no longer divisible by the current divisor, increment the divisor
        divisor += 1

    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script works by dividing the input number `n` by the smallest divisor (2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will necessarily be a prime number. This process continues until `n` is reduced to 1. The list of divisors that were used to reduce `n` to 1 are the prime factors of `n`.