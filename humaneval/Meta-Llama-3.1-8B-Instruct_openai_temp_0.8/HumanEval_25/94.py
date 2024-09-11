### Prime Factorization Script

Below is a simple Python script that uses a helper function to check if a number is prime, and another function to perform prime factorization.

```python
from typing import List

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0 and is_prime(divisor):
            count = 0
            while n % divisor == 0:
                count += 1
                n = n // divisor
            factors.extend([divisor] * count)
        divisor += 1
    return factors

# Example use cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a simple trial division approach to check for primality and to perform prime factorization. The `is_prime` function checks if a number is divisible by any number up to its square root to determine if it's prime. The `factorize` function iterates from 2 to the input number, checking for divisibility and primality, and adds the divisor to the list of factors as many times as it appears in the factorization.