```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to be factorized.

    Returns:
        List[int]: A list of prime factors of the input number.
    """
    factors = []
    while n % 2 == 0:
        # If the number is divisible by 2, it's a prime factor
        factors.append(2)
        n = n // 2

    # Check for odd factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If the remaining number is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This Python script uses a simple algorithm to find the prime factors of a given integer. It starts by checking for divisibility by 2, then moves on to odd numbers up to the square root of the input number. If the remaining number is a prime number greater than 2, it's added to the list of factors. The function returns the list of prime factors in the order they appear.