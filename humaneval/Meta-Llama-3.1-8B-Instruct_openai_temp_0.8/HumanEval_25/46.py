### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized

    Returns:
        List[int]: A list of prime factors
    """
    factors = []
    i = 2
    while n > 1:
        # If n is divisible by i, then i is a prime factor
        if n % i == 0:
            # Count the occurrences of i in factors
            count = 0
            while n % i == 0:
                n = n // i
                count += 1
            # Add i to factors, count times
            factors.extend([i] * count)
        # Move to the next number
        i += 1
    return factors

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a `factorize` function that takes an integer `n` as input and returns a list of its prime factors. The function uses a simple trial division method to find the prime factors, where it checks each number up to the square root of `n` to see if it divides `n` evenly. If it does, it counts the number of times it divides `n` evenly and adds that many instances of the number to the list of factors.

The script also includes example usage at the end to demonstrate how to use the `factorize` function.