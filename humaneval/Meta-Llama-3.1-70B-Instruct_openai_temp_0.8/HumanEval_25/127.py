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
        # If n is divisible by divisor, then it's a factor
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        # If not, increment divisor by 1
        divisor += 1
    return factors

# Test cases
assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]
assert factorize(100) == [2, 2, 5, 5]
assert factorize(1) == []
```

This script defines a function `factorize(n)` that finds all prime factors of a given integer `n`. The function starts by initializing an empty list `factors` to store the prime factors, and a variable `divisor` to 2, which is the smallest prime number.

The function enters a while loop that continues until `n` is reduced to 1. Inside the loop, it checks if `n` is divisible by `divisor`. If it is, `divisor` is a factor of `n`, so it's appended to the `factors` list and `n` is divided by `divisor`. This process continues until `n` is no longer divisible by `divisor`.

If `n` is not divisible by `divisor`, the function increments `divisor` by 1 and repeats the process. This continues until `n` is reduced to 1, at which point the function returns the list of prime factors.

The script includes test cases to verify the correctness of the function.