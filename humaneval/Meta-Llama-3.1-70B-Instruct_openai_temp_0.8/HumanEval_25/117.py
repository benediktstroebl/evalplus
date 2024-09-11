```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input number to be factorized

    Returns:
        List[int]: List of prime factors in the order from smallest to largest
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
    for possible_prime in range(2, n + 1):
        # Check if the possiblePrime is indeed a prime number
        if is_prime(possible_prime):
            # Check if the number is divisible by the prime
            while n % possible_prime == 0:
                # If it is, add it to the factors and divide the number
                factors.append(possible_prime)
                n = n // possible_prime
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script first defines a helper function `is_prime` to check whether a number is prime. Then it defines the `factorize` function, which finds all prime factors of the input number. The `factorize` function uses a loop to check each number up to the input number to see if it is prime and if the input number is divisible by it. If both conditions are met, the number is added to the list of factors and the input number is divided by it. This process continues until the input number is reduced to 1. The function then returns the list of prime factors.