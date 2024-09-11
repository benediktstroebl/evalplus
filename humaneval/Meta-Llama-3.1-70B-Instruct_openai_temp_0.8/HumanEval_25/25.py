```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Number to be factorized.

    Returns:
        List[int]: List of prime factors.
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        # If n is divisible by divisor, add it to the factors and divide n by divisor
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If divisor is not a factor, increment it
        divisor += 1
        # If divisor is not prime, increment it until we find a prime number
        while not is_prime(divisor):
            divisor += 1
    return factors


# Test cases
print(factorize(8))    # [2, 2, 2]
print(factorize(25))   # [5, 5]
print(factorize(70))   # [2, 5, 7]
```

This script uses a helper function `is_prime` to check if a number is prime. The `factorize` function starts by dividing the input number `n` by the smallest prime number (2), and continues dividing `n` by the smallest prime divisor until `n` is no longer divisible by that divisor. It then increments the divisor until it finds the next prime number, and repeats the process until `n` is reduced to 1. The list of divisors is returned as the result.