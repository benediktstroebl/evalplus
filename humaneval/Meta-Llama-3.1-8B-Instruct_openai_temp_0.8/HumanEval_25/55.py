### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The input number to factorize.

    Returns:
        List[int]: A list of prime factors of the input number.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script uses a simple trial division method to find the prime factors of the input number. It starts from 2 and checks if the input number is divisible by the current number. If it is, it divides the input number by the current number and adds the current number to the list of factors. It continues this process until the input number is reduced to 1. If the input number is a prime number, it is added to the list of factors as it is.