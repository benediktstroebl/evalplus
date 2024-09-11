### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input integer to factorize

    Returns:
        List[int]: List of prime factors of n
    """
    factors = []
    i = 2
    while n > 1:
        # Check if i is a factor of n
        while n % i == 0:
            # If i is a factor, add it to the list and divide n by i
            factors.append(i)
            n = n // i
        # Increment i by 1
        i += 1
    return factors

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This script uses a simple trial division method to factorize the input number `n`. It starts by checking if `n` is divisible by 2, then by 3, and so on, until it finds a prime factor. Once a prime factor is found, it continues dividing `n` by that factor until it is no longer divisible. This process is repeated until `n` is reduced to 1. The resulting list of factors is then returned.