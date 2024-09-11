```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns a list of prime factors of the given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors of the given integer.

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

# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

In this script, we define a function `factorize(n)` that returns a list of prime factors of the given integer `n`. The function uses a while loop to iterate through all numbers from 2 to the square root of `n`. If `n` is divisible by the current number `i`, we divide `n` by `i` and add `i` to the list of factors. If `n` is not divisible by `i`, we increment `i` by 1. After the loop, if `n` is greater than 1, it means that `n` is a prime number and we add it to the list of factors. Finally, we return the list of factors.