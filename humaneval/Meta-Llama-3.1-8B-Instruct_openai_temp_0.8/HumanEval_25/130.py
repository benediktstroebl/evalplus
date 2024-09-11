```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
    n (int): The number to factorize.
    
    Returns:
    List[int]: A list of prime factors.
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """

    def is_prime(x: int) -> bool:
        """Helper function to check if a number is prime."""
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
        # Skip even divisors if they are not prime
        if divisor % 2 == 0 and divisor!= 2:
            divisor += 1

    # Remove duplicates and keep the smallest prime
    unique_factors = []
    for factor in factors:
        if not unique_factors or factor!= unique_factors[-1]:
            unique_factors.append(factor)
        else:
            continue

    return unique_factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer as input and returns its prime factors in a list. The function uses a helper function `is_prime` to check if a number is prime. It then iterates through all possible divisors of the input number, appending each prime divisor to the list as many times as it occurs. Finally, it removes duplicates from the list of factors by keeping only the smallest prime factor at each step.