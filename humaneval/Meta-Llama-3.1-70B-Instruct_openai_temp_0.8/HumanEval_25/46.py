```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize

    Returns:
        List[int]: A list of prime factors
    """
    # Initialize an empty list to store the factors
    factors = []
    # Initialize the divisor to 2 (the smallest prime number)
    divisor = 2
    
    # Continue dividing the number until it's reduced to 1
    while n > 1:
        # If the number is divisible by the current divisor, it's a factor
        if n % divisor == 0:
            # Add the factor to the list
            factors.append(divisor)
            # Divide the number by the factor
            n = n // divisor
        else:
            # If the number is not divisible by the current divisor, increment the divisor
            divisor += 1
    
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines the `factorize` function, which takes an integer `n` and returns a list of its prime factors. The function uses a while loop to divide the number by increasing divisors until it's reduced to 1. The divisors that divide the number evenly are added to the list of factors. The function returns the list of factors. The script also includes test cases to verify the function's correctness.