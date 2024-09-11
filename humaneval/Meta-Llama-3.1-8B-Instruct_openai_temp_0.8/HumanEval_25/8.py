### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The input number to factorize.

    Returns:
    List[int]: A list of prime factors in the order from smallest to largest.

    Raises:
    ValueError: If the input number is less than 2.

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """

    if n < 2:
        raise ValueError("Input number should be greater than or equal to 2")

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


if __name__ == "__main__":
    # Test cases
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
    print(factorize(13))  # [13]
    print(factorize(100)) # [2, 2, 5, 5]
```
This script uses a simple trial division method to find the prime factors of a given number. It starts by checking the smallest prime number (2) and increments the divisor until it finds one that divides the number evenly. If it finds a divisor, it divides the number by that divisor and adds the divisor to the list of factors. This process continues until the number is reduced to 1. The result is a list of prime factors in the order from smallest to largest.