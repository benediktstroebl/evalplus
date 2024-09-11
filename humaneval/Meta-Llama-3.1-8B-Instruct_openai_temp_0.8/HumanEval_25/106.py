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
        List[int]: A list of prime factors of the given integer.
    """
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors


# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a simple trial division approach to find the prime factors of a given number. It iteratively divides the input number `n` by the smallest divisor that can divide it without leaving a remainder, which is `2` in this case. If `n` is divisible by the divisor, it adds the divisor to the list of factors and divides `n` by the divisor. This process continues until `n` is reduced to `1`. If `n` is a prime number itself, the while loop for the divisor will simply increment the divisor until it's greater than n.