```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: Input integer
    :return: List of prime factors
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

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

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors. The function uses a helper function `is_prime` to check if a number is prime. However, in this case, we don't actually need to check if a number is prime because we're iterating from 2 upwards and only appending numbers that divide `n` evenly.

The `factorize` function works by dividing `n` by the smallest prime factor (which is 2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will necessarily be a prime factor. This process continues until `n` is reduced to 1. The remaining `n` is appended to the list of factors if it's greater than 1.

The test cases at the end verify that the function works correctly for the given examples.