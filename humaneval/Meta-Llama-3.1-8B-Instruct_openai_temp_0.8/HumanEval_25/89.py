```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize

    Returns:
        List[int]: A list of prime factors of the input number

    Examples:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 2, 5, 7]
    """

    # Initialize an empty list to store the prime factors
    factors = []

    # Initialize the divisor to 2, which is the smallest prime number
    divisor = 2

    # While the number is greater than 1, we continue to divide it by the divisor
    while n > 1:
        # If the number is divisible by the divisor, then the divisor is a factor
        if n % divisor == 0:
            # We add the divisor to the list of factors
            factors.append(divisor)
            # And we divide the number by the divisor
            n = n // divisor
        else:
            # If the number is not divisible by the divisor, then we increment the divisor by 1
            divisor += 1

    # We use a list comprehension to group the factors by their value
    # This is because we want to list each factor the number of times it appears in the factorization
    factors = [f for f in set(factors) for _ in range(factors.count(f))]

    return factors

# Test the function
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 2, 5, 7]
```

This script first initializes an empty list to store the prime factors and a divisor to 2. It then enters a loop that continues as long as the input number is greater than 1. Inside the loop, it checks if the number is divisible by the divisor. If it is, it adds the divisor to the list of factors and divides the number by the divisor. If it is not, it increments the divisor by 1. After the loop, it uses a list comprehension to group the factors by their value, so that each factor appears the number of times it appears in the factorization.