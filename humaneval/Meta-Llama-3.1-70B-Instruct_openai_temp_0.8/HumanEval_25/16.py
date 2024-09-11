```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to be factorized.

    Returns:
        List[int]: A list of prime factors in the order from smallest to largest.
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
        # If n is divisible by divisor, it is a factor
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If divisor is not a factor, increment it by 1
        divisor += 1
        # If divisor is not prime, increment it until we find a prime number
        while not is_prime(divisor):
            divisor += 1
    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```