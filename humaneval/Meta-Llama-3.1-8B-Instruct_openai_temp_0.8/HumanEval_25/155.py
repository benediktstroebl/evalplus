```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    Args:
    n (int): The input number to be factorized
    
    Returns:
    List[int]: A list of prime factors of the input number
    """
    
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize result list and divisor
    factors = []
    divisor = 2
    
    # Loop until n is reduced to 1
    while n > 1:
        # Check if n is divisible by the current divisor
        if n % divisor == 0:
            # If divisible, append divisor to result list and divide n
            factors.append(divisor)
            n = n // divisor
        else:
            # If not divisible, increment divisor
            divisor += 1
        # Ensure divisor is still a prime number
        while not is_prime(divisor):
            divisor += 1
    
    return factors

# Example usage:
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

In this script, the `factorize` function takes an integer `n` and returns its prime factors. It uses a helper function `is_prime` to check if a number is prime. The `factorize` function works by continuously dividing `n` by the smallest divisor (which starts at 2) until it is no longer divisible. The divisor is then added to the result list, and the process is repeated until `n` is reduced to 1. The result list contains the prime factors of `n` in the order from smallest to largest.