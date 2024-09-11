### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns a list of prime factors of a given integer in the order from smallest to largest.
    Each of the factors is listed the number of times corresponding to how many times it appears in the factorization.
    Input number should be equal to the product of all factors.

    Parameters:
    n (int): The number to be factorized.

    Returns:
    List[int]: A list of prime factors.
    """
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    return factors

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This script works by continuously dividing the input number `n` by the smallest prime number (2) as long as it's divisible. If it's not divisible by 2, it increments the divisor by 1 until it finds a divisor. This process continues until `n` is reduced to 1, at which point the list of factors is returned.

Note that this script assumes that the input number `n` is a positive integer. If you need to handle negative integers or non-integer input, you'll need to modify the script accordingly.