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
    def prime_factors(num: int) -> List[int]:
        factors = []
        i = 2
        while num > 1:
            if num % i == 0:
                factors.append(i)
                num //= i
            else:
                i += 1
        return factors

    return prime_factors(n)


# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that calculates the prime factorization of a given integer. It uses a helper function `prime_factors` to find all prime factors of a number by dividing it by the smallest divisor (starting from 2) until it's no longer divisible. The result is a list of prime factors in ascending order, where each factor appears as many times as it appears in the factorization.

The `factorize` function then simply calls `prime_factors` with the input number `n` and returns the result.

The script also includes some test cases at the end to verify that the `factorize` function works correctly.