```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors.
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            # Check if divisor is prime before adding it to the list
            if is_prime(divisor):
                factors.append(divisor)
                n = n // divisor
            else:
                # If divisor is not prime, increment it
                divisor += 1
        else:
            # If n is not divisible by divisor, increment divisor
            divisor += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime. It iterates over all numbers starting from 2, checks if the current number is a divisor of `n`, and if it is, checks if it is prime before adding it to the list of factors. The process continues until `n` is reduced to 1. The test cases at the end demonstrate the usage of the `factorize` function.