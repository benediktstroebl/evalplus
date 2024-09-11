```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    # Initialize an empty list to store the prime factors
    factors = []
    
    # Initialize the divisor to 2 (smallest prime number)
    divisor = 2
    
    # Continue the loop until n is greater than 1
    while n > 1:
        # If n is divisible by the current divisor, it is a prime factor
        if n % divisor == 0:
            # Append the divisor to the list of factors
            factors.append(divisor)
            # Divide n by the divisor to find the next factor
            n = n // divisor
        else:
            # If the current divisor is not a factor, increment it by 1
            divisor += 1
    
    # Return the list of prime factors
    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```