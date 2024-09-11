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
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors

# Example usage:
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This script works by initializing a list `factors` to store the prime factors. The variable `divisor` is used to test for factors, starting at 2 (the smallest prime number). The loop continues as long as `n` is greater than 1.

Inside the loop, the script checks whether `n` is divisible by `divisor`. If it is, `divisor` is added to the `factors` list, and `n` is divided by `divisor` (integer division to avoid fractional results). This effectively removes the factor `divisor` from `n`.

After checking all possible factors, the `divisor` is incremented by 1 and the loop repeats. The loop exits when `n` is reduced to 1, at which point all factors have been found.

The script returns the list of prime factors.