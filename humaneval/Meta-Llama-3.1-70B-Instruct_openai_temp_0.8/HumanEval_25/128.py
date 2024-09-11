```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: Input number
    :return: List of prime factors
    """
    factors = []
    i = 2
    # Iterate over all numbers until the square root of n
    while i * i <= n:
        # If n is divisible by i, then i is a factor
        if n % i:
            # If not, increment i by 1
            i += 1
        else:
            # If it is, divide n by i and add i to the list of factors
            n //= i
            factors.append(i)
    # If n is not 1 at this point, it is a prime factor
    if n > 1:
        factors.append(n)
    return factors

# Example use cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. It iterates over all numbers from 2 up to the square root of `n`, checks if `n` is divisible by the current number, and if it is, adds it to the list of factors and divides `n` by it. If `n` is not divisible by any number up to its square root, it is a prime factor itself and is added to the list. The function returns the list of prime factors.

The script also includes some example use cases to demonstrate how to use the `factorize` function.