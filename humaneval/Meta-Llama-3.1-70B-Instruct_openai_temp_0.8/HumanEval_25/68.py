```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to be factorized

    Returns:
    List[int]: List of prime factors
    """
    # Initialize an empty list to store the prime factors
    factors = []

    # Initialize the divisor to 2 (the smallest prime number)
    divisor = 2

    # Continue the loop until the number is completely factorized
    while n > 1:
        # If the number is divisible by the current divisor, it's a prime factor
        if n % divisor == 0:
            # Add the prime factor to the list
            factors.append(divisor)
            # Divide the number by the prime factor
            n = n // divisor
        else:
            # If the current divisor doesn't divide the number, increment it by 1
            divisor += 1

    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines the `factorize` function that takes an integer `n` as input and returns a list of its prime factors. The function iteratively divides the input number `n` by the smallest divisor (starting from 2) until `n` is completely factorized. The prime factors are stored in a list and returned at the end.