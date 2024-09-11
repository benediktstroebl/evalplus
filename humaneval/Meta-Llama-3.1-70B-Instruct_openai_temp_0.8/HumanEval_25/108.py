```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
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
    divisor = 2
    while n > 1:
        # Check if the current divisor is a factor of n
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If the current divisor is not a factor, increment it
        divisor += 1
        # If the current divisor is not prime, increment it to the next prime number
        while not is_prime(divisor):
            divisor += 1

    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```