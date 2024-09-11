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
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple algorithm to factorize the given number. It starts by dividing the number by the smallest prime number (2) as long as it's divisible. Then it increments the divisor by 1 and repeats the process until the divisor is greater than the square root of the number. If the number is not divisible by the current divisor, it simply increments the divisor by 1. Once the loop finishes, if the remaining number is greater than 1, it means that the remaining number is a prime factor, and it's appended to the list of factors.