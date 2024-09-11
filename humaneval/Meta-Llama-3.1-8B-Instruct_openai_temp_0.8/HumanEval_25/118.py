### Factorization of an Integer
#### Problem Description
This script solves the problem of factorizing an integer into its prime factors.

#### Code
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns a list of prime factors of the given integer in the order from smallest to largest.
    Each of the factors is listed a number of times corresponding to how many times it appears in the factorization.
    The input number should be equal to the product of all factors.

    Args:
        n (int): The number to be factorized.

    Returns:
        List[int]: A list of prime factors of the given integer.

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
    while n > 1:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    return factors

# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

#### Explanation
The provided code defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function uses a simple trial division method to find the prime factors.

Here's a step-by-step breakdown of how the code works:

1.  Initialize an empty list `factors` to store the prime factors.
2.  Initialize a variable `i` to 2, which will be used to check if `n` is divisible by `i`.
3.  Enter a while loop that continues until `n` becomes 1.
4.  Inside the loop, check if `n` is divisible by `i` using the modulo operator (`n % i == 0`).
5.  If `n` is divisible by `i`, then `i` is a prime factor of `n`. Divide `n` by `i` and append `i` to the `factors` list.
6.  If `n` is not divisible by `i`, increment `i` by 1.
7.  Once the loop completes, return the `factors` list, which contains the prime factors of the original input number.

This code provides a simple and efficient solution to the problem of factorizing an integer into its prime factors.