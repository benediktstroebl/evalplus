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
        List[int]: A list of prime factors in the order from smallest to largest
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            # If i is a prime factor, append it to the list and divide n by i
            factors.append(i)
            n = n // i
        else:
            # If i is not a prime factor, increment it by 1
            i += 1
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a helper function `is_prime` to check if a number is prime. The `factorize` function then iterates over numbers from 2 to `n` (inclusive), and for each number, it checks if it is a prime factor of `n`. If it is, it appends the number to the list of factors and divides `n` by that number. If it is not a prime factor, it increments the number by 1. This process continues until `n` is reduced to 1, at which point the list of factors is returned.