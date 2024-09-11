```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to be factorized.

    Returns:
        List[int]: A list of prime factors of the input number.
    """
    def is_prime(x: int) -> bool:
        """Check if number is prime."""
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a helper function `is_prime(x)` to check whether a number is prime. It then iterates from 2 up to the square root of the input number `n`, checking for divisibility. If `n` is divisible by `i`, it appends `i` to the list of factors and divides `n` by `i`. This process continues until `n` is reduced to 1. If `n` is still greater than 1 at the end, it means that `n` is a prime number greater than the square root of the original input, so it is appended to the list of factors.