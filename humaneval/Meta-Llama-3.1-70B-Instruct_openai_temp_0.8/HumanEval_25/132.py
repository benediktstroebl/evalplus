```python
from typing import List

def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors"""
    
    # Initialize an empty list to store the prime factors
    prime_factors = []
    
    # Initialize a divisor to 2 (the smallest prime number)
    divisor = 2
    
    # Continue the loop until n is greater than 1
    while n > 1:
        # If n is divisible by the current divisor, it is a prime factor
        if n % divisor == 0:
            # Append the divisor to the list of prime factors
            prime_factors.append(divisor)
            # Divide n by the divisor
            n = n // divisor
        else:
            # If n is not divisible by the current divisor, increment the divisor
            divisor += 1
    
    return prime_factors


# Test cases
print(factorize(8))   # Expected output: [2, 2, 2]
print(factorize(25))  # Expected output: [5, 5]
print(factorize(70))  # Expected output: [2, 5, 7]
```