```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
    n (int): The number to be factorized.
    
    Returns:
    List[int]: A list of prime factors of the input number.
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    
    # Initialize an empty list to store prime factors
    factors = []
    
    # Initialize a divisor to 2 (the smallest prime number)
    divisor = 2
    
    # Continue the loop until the number is reduced to 1
    while n > 1:
        
        # If the number is divisible by the current divisor, then the divisor is a prime factor
        while n % divisor == 0:
            # Append the divisor to the list of factors
            factors.append(divisor)
            # Divide the number by the divisor
            n = n // divisor
        
        # Increment the divisor by 1
        divisor += 1
    
    # Return the list of prime factors
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The prime factors are listed in increasing order and each factor appears as many times as it appears in the factorization of `n`. The script uses a while loop to repeatedly divide `n` by the smallest divisor that divides it, which is 2, until `n` is reduced to 1. The divisors that divide `n` are added to the list of factors. The function then returns the list of factors.