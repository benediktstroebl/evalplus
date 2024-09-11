### Prime Factorization Implementation in Python

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input integer to be factorized

    Returns:
        List[int]: List of prime factors of input integer

    Example:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
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

# Test the function
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of a given integer. It starts by dividing the input number by 2, then increments the divisor until it finds the next prime factor. This process continues until the input number is reduced to 1. The prime factors are then added to the result list. If the remaining number is a prime number greater than 1, it is also added to the result list.