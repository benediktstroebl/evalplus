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
        """
        Helper function to check if a number is prime
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            count = 0
            while n % i == 0:
                n = n // i
                count += 1
            factors.extend([i] * count)
        i += 1
    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a helper function `is_prime` to check if a number is prime, and the main function `factorize` to find the prime factors of a given number. The `factorize` function uses a while loop to keep dividing the input number `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. It keeps track of the number of times `i` divides `n` and adds `i` to the list of factors that many times. If `i` is not prime, the function increments it by 1. The loop continues until `n` is reduced to 1. The list of factors is then returned.