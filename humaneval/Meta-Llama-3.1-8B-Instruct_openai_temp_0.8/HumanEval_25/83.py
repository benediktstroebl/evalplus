```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
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

# Example usage
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. Each factor is listed the number of times it appears in the factorization.

The function uses a simple trial division approach to find the factors. It starts by dividing the input number by the smallest prime number (2) as long as it is divisible. Then it increments the divisor until it finds the next number that can divide the input number, which is a prime factor. This process continues until the input number is reduced to 1. If the last remaining number is greater than 1, it is a prime number and is added to the list of factors.

The example usage at the end of the script demonstrates how to use the `factorize(n)` function to find the prime factors of different numbers.