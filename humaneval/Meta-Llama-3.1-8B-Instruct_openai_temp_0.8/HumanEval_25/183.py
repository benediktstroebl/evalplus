### Prime Factorization Script

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to factorize.

    Returns:
    List[int]: A list of prime factors.
    """

    # Initialize an empty list to store prime factors
    factors = []

    # Iterate over all numbers from 2 to n (inclusive)
    for i in range(2, n + 1):
        # If n is divisible by i, then i is a factor
        while n % i == 0:
            # Add i to the list of factors
            factors.append(i)
            # Divide n by i to remove the factor
            n = n // i

    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find all prime factors of a given number. The `while` loop inside the `for` loop checks if the current number is a factor of `n`, and if it is, the number is added to the list of factors and `n` is divided by this number. This process is repeated until `n` is reduced to 1. The resulting list of factors is then returned.