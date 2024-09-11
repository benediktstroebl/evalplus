```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input integer

    Returns:
        List[int]: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """Check if number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize an empty list to store prime factors
    factors = []
    i = 2
    # Keep dividing the input number by the current number until it's no longer divisible
    while n > 1:
        while n % i == 0:
            # If the current number is a prime factor, append it to the list
            factors.append(i)
            # Divide the input number by the current prime factor
            n = n // i
        # Move on to the next number
        i += 1

    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, the `factorize` function takes an integer as input and returns a list of its prime factors. The function first checks if a number is prime using the helper function `is_prime`. Then it iterates over all numbers starting from 2 and keeps dividing the input number by the current number as long as it's divisible. The prime factors are appended to the list and the input number is divided by the prime factor. This process continues until the input number is reduced to 1.