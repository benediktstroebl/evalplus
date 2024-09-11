```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    def get_prime_factors(num: int) -> List[int]:
        i = 2
        factors = []
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        return factors

    return get_prime_factors(n)


# Example usage:
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors. The function uses a helper function `get_prime_factors` to generate the prime factors.

The `get_prime_factors` function works by dividing the input number `num` by the smallest divisor `i` (starting from 2) until `num` is reduced to 1. If `num` is divisible by `i`, it is divided by `i` and `i` is added to the list of factors. If `num` is not divisible by `i`, `i` is incremented by 1. The last remaining number (which is a prime factor greater than 1) is also added to the list of factors.

The `factorize` function simply calls `get_prime_factors` with the input number `n` and returns the result.

The script also includes some example usage to demonstrate how the `factorize` function works.