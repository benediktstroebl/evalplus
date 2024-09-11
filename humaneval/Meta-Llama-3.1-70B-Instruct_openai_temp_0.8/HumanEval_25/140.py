```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num: int) -> List[int]:
        """Get prime factors of a number"""
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
if __name__ == "__main__":
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
```
This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. It uses two helper functions: `is_prime` checks if a number is prime, and `get_prime_factors` finds all prime factors of a number. The test cases at the end verify that the `factorize` function works correctly.