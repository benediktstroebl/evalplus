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
        List[int]: A list of prime factors of the number
    """
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
print(factorize(100)) # [2, 2, 5, 5]
```
This script uses a simple iterative approach to find the prime factors of a given number. It starts with the smallest prime number, 2, and checks if it can divide the number without a remainder. If it can, it adds the divisor to the list of factors and divides the number by the divisor. If it can't, it increments the divisor and checks again. This process continues until the number is reduced to 1, at which point all of its prime factors have been found.