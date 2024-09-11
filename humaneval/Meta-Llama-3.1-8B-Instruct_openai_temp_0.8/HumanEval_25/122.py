### Factorization of Integers
#### Solution in Python
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Parameters:
    n (int): Integer to factorize
    
    Returns:
    List[int]: List of prime factors of the input integer
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    i = 2  # Initialize divisor to 2 (smallest prime number)
    factors = []  # Initialize list to store prime factors
    
    while n > 1:  # Continue until n is reduced to 1
        while n % i == 0:  # If n is divisible by i, it's a prime factor
            factors.append(i)  # Add i to the list of factors
            n = n // i  # Divide n by i to reduce its value
        i += 1  # Increment divisor by 1 for next iteration
        
    return factors  # Return the list of prime factors

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function uses a simple trial division method to find prime factors, where it repeatedly divides the input number `n` by the smallest divisor `i` (starting from 2) until `n` is reduced to 1. Each time a divisor `i` is found, it's added to the list of factors and `n` is divided by `i` to proceed with the next iteration.