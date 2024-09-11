```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
    n (int): The input number to be factorized.
    
    Returns:
    List[int]: A list of prime factors.
    """
    
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.
        
        Args:
        num (int): The number to be checked.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            while n % i == 0:
                n //= i
                factors.append(i)
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer as input and returns its prime factors. The function uses a helper function `is_prime` to check if a number is prime. The `factorize` function iterates through numbers from 2 to the input number, checks if the current number is a factor and if it's prime, and if so, adds it to the list of factors and divides the input number by this factor. The process continues until the input number is reduced to 1. The test cases at the end of the script demonstrate the function's usage.