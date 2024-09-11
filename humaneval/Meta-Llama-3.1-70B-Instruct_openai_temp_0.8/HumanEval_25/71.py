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
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple iterative approach to find the prime factors of a given number. It starts by dividing the number by the smallest prime number (2), and continues to divide the number by the smallest divisor until it is no longer divisible. It then increments the divisor and repeats the process until the number is reduced to 1. The list of divisors that were used to reduce the number to 1 are the prime factors of the original number.