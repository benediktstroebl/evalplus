```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
    n (int): The number to be factorized.
    
    Returns:
    List[int]: A list of prime factors.
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        # If n is divisible by the current divisor, it's a factor
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If the current divisor is prime, increment it
        if is_prime(divisor):
            divisor += 1
        # If the current divisor is not prime, find the next prime number
        else:
            divisor += 1
            while not is_prime(divisor):
                divisor += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a helper function `is_prime` to check whether a number is prime. The main function iterates through numbers starting from 2, checks if the current number is a factor of `n`, and if so, divides `n` by this factor and adds it to the list of factors. The process continues until `n` is reduced to 1. The script also includes test cases to verify the correctness of the function.