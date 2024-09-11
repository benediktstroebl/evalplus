```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input integer to be factorized

    Returns:
        List[int]: List of prime factors of the input integer
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

# Example use cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
print(factorize(100))  # [2, 2, 5, 5]
```

This script uses a simple trial division algorithm to find the prime factors of the input integer. It starts by dividing the number by 2, and if it's divisible, it adds 2 to the list of factors and divides the number by 2. It continues this process with increasing integers until it finds a prime factor. If the number is not divisible by any of these integers, it increments the integer by 1. This process continues until the number is reduced to 1, which means all its prime factors have been found.