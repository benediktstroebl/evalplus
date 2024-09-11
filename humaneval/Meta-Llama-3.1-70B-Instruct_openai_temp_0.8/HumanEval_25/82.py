```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors.

    Examples:
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

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of a given number `n`. The function `factorize` takes an integer `n` as input and returns a list of its prime factors in ascending order, where each factor appears as many times as it does in the prime factorization of `n`.

Here's how it works:

1. Initialize an empty list `factors` to store the prime factors.
2. Initialize a variable `i` to 2, which is the smallest prime number.
3. As long as `i` squared is less than or equal to `n`, check if `n` is divisible by `i`.
   - If `n` is not divisible by `i`, increment `i` by 1.
   - If `n` is divisible by `i`, divide `n` by `i` and append `i` to the `factors` list.
4. If `n` is greater than 1 after the loop, it means that `n` itself is a prime factor, so append `n` to the `factors` list.
5. Return the `factors` list.

The script includes test cases to verify that the function works correctly.