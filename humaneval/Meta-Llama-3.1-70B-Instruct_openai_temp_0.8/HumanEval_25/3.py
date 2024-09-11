```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: The number to be factorized
    :return: List of prime factors
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

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script uses a simple trial division method to find the prime factors of a given number. It starts by dividing the input number `n` by the smallest prime number (2), and continues dividing by the smallest divisor until it is no longer divisible. It then increments the divisor until it finds the next number that can divide `n`, which will be a prime number. This process continues until `n` is reduced to 1. The list of divisors that were used to reduce `n` to 1 are the prime factors of `n`.