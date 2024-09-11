```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize

    Returns:
        List[int]: A list of prime factors

    Example:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    i = 2  # Start with the first prime number
    factors = []
    while i * i <= n:  # Only need to check up to the square root of n
        if n % i:  # If n is not divisible by i
            i += 1
        else:  # If n is divisible by i
            n //= i
            factors.append(i)
    if n > 1:  # If n is a prime number greater than 1
        factors.append(n)
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of prime factors of `n`. The function uses a simple trial division method to find the prime factors, which is efficient for small to medium-sized integers. The function is tested with three example inputs to verify that it produces the correct results.