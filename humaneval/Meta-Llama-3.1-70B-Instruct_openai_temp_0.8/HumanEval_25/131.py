```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        # check if i is a factor of n
        while n % i == 0:
            # check if i is prime
            if is_prime(i):
                factors.append(i)
                n = n // i
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script works by dividing the input number `n` by the smallest prime factor `i` until it's no longer divisible. It checks if `i` is prime by calling the helper function `is_prime()`. If `i` is prime, it appends `i` to the list of factors and divides `n` by `i`. The process continues until `n` is reduced to 1.