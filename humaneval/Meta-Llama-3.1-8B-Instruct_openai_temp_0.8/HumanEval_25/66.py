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
    print(factorize(8))   # Output: [2, 2, 2]
    print(factorize(25))  # Output: [5, 5]
    print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize(n)` that returns a list of prime factors of the input integer `n`. The function uses a simple loop to divide the input number by the smallest divisor (starting from 2) until it is no longer divisible. The divisor is then added to the list of factors. This process continues until the input number is reduced to 1. If the input number is a prime number (greater than 1), it is added to the list of factors at the end. The function returns the list of factors in the order they appear.