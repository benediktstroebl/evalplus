### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to factorize

    Returns:
    List[int]: A list of prime factors

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    i = 2
    factors = []
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
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

This script defines a `factorize` function that takes an integer `n` and returns a list of its prime factors. The function works by incrementally dividing the input number `n` by the smallest divisor `i`, which is initially set to 2. If `n` is divisible by `i`, the divisor `i` is added to the list of factors and `n` is divided by `i` until it is no longer divisible. This process continues until `n` is reduced to 1. If `n` is greater than 1 at the end of the process, it means that `n` itself is a prime number and is added to the list of factors. The function returns the list of prime factors.

The example usage at the end of the script demonstrates how to use the `factorize` function to factorize the numbers 8, 25, and 70.