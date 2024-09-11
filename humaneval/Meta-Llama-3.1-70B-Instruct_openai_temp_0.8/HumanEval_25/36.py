```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Initialize an empty list to store the prime factors
    factors = []
    # Initialize the divisor to 2 (the smallest prime number)
    divisor = 2

    # Continue dividing the number until it's reduced to 1
    while n > 1:
        # If the number is divisible by the current divisor, it's a prime factor
        if n % divisor == 0:
            # Add the prime factor to the list
            factors.append(divisor)
            # Divide the number by the prime factor
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

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in ascending order. The function uses a simple trial division method to find the prime factors, starting from the smallest prime number (2). The test cases at the end demonstrate the function's correctness.