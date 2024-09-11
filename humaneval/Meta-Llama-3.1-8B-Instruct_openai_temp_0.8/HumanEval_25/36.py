```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input integer to be factorized.

    Returns:
        List[int]: List of prime factors.
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


# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple algorithm to factorize the input number `n`. It iterates over all numbers from 2 (the smallest prime) up to the square root of `n`, checking if the current number is a factor of `n`. If it is, it repeatedly divides `n` by the factor until `n` is no longer divisible by the factor. The factor is then added to the list of factors. If `n` itself is a prime number greater than 1, it is also added to the list of factors.