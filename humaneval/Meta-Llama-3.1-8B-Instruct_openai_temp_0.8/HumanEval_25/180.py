**Prime Factorization in Python**
=====================================

### Code
```python
from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
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


# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
### Explanation

This script uses a simple trial division method to find the prime factors of a given integer. Here's a step-by-step breakdown of the code:

1. Initialize an empty list `factors` to store the prime factors.
2. Start with `i = 2`, the smallest prime number.
3. While `i` squared is less than or equal to the input number `n`, check if `n` is divisible by `i`.
4. If `n` is not divisible by `i`, increment `i` by 1.
5. If `n` is divisible by `i`, divide `n` by `i` and append `i` to the `factors` list.
6. Repeat steps 3-5 until `i` squared is greater than `n`.
7. If `n` is greater than 1 at this point, it means `n` is a prime number and append it to the `factors` list.
8. Return the `factors` list, which contains the prime factors of the input number in the order from smallest to largest.