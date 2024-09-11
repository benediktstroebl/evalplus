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
    """
    # Initialize an empty list to store the prime factors
    factors = []

    # Initialize a divisor to 2 (the smallest prime number)
    divisor = 2

    # Continue the loop until the divisor is less than or equal to n
    while divisor <= n:
        # If n is divisible by the divisor, it's a prime factor
        if n % divisor == 0:
            # Append the divisor to the list of factors
            factors.append(divisor)
            # Divide n by the divisor to remove it as a factor
            n = n // divisor
        else:
            # If the divisor is not a factor, increment it by 1
            divisor += 1

    # Return the list of prime factors
    return factors

# Test the function
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize(n: int) -> List[int]` that takes an integer `n` as input and returns a list of its prime factors. The function uses a simple trial division method to find the prime factors, starting from the smallest prime number (2) and incrementing the divisor until it finds a factor. The script then tests the function with the provided example inputs.