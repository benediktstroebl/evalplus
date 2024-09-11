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
    factors = []
    i = 2
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
print(factorize(8))    # Output: [2, 2, 2]
print(factorize(25))   # Output: [5, 5]
print(factorize(70))   # Output: [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. It uses a simple trial division method to find the factors. The loop starts from the smallest prime number (2) and checks divisibility of `n` with the current number. If `n` is divisible, it appends the divisor to the `factors` list and divides `n` by the divisor. This process continues until `n` is reduced to 1. Finally, if `n` is still greater than 1, it means `n` itself is a prime number and is appended to the `factors` list.