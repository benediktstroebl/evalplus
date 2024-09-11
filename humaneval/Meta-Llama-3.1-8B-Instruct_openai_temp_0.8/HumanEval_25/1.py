```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to factorize

    Returns:
        List[int]: A list of prime factors of the input number

    Example:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of a given number. It iterates from 2 to the square root of the number, dividing the number by each potential factor. If the number is divisible, it adds the factor to the list and divides the number by the factor. If it reaches a number that is not divisible by any potential factor, it adds the number to the list as it is a prime factor. The function finally returns the list of prime factors.