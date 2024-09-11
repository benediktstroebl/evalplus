```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num: int) -> List[int]:
        """
        Helper function to get prime factors of a number
        """
        factors = []
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                factors.append(i)
                num //= i
                while num % i == 0:
                    factors.append(i)
                    num //= i
        return factors

    return get_prime_factors(n)


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a `factorize` function that takes an integer `n` as input and returns a list of its prime factors. The function uses two helper functions: `is_prime` to check if a number is prime, and `get_prime_factors` to get the prime factors of a number.

The `get_prime_factors` function iterates over the numbers from 2 to `n` and checks if each number is a prime factor of `n`. If it is, the function appends the number to the list of factors and divides `n` by the number. This process continues until `n` is reduced to 1.

The `factorize` function simply calls `get_prime_factors` and returns the result.