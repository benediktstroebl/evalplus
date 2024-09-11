```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: The number to factorize
    :return: A list of prime factors
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

# Example use cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in ascending order. The function works by dividing the input number `n` by the smallest prime number (2) as long as it's divisible, then incrementing the divisor until it finds the next number that can divide `n`, which will necessarily be a prime number. This process continues until `n` is reduced to 1. The list of divisors obtained through this process will be the list of prime factors of the original number.