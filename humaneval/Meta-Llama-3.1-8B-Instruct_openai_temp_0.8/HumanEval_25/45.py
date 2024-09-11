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
    List[int]: A list of prime factors of the given integer
    """
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

# Test cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script works by continuously checking if `n` is divisible by `i`, starting from `i = 2`. If it is, then we divide `n` by `i` and add `i` to our list of factors. If `n` is not divisible by `i`, then we increment `i` by 1. This process continues until `i` is greater than the square root of `n`. If `n` is still greater than 1 after this process, then it means that `n` is a prime number and we add it to our list of factors.