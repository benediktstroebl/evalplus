**Prime Factorization of an Integer**
=====================================

The following Python script defines a function `factorize(n)` that returns a list of prime factors of a given integer `n`. The function uses a helper function `is_prime(x)` to check if a number is prime.

```python
from typing import List

def is_prime(x: int) -> bool:
    """
    Check if a number is prime.

    Args:
    x (int): The number to check.

    Returns:
    bool: True if x is prime, False otherwise.
    """
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.

    Args:
    n (int): The number to factorize.

    Returns:
    List[int]: A list of prime factors.
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

# Example use cases
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of a given number. The `is_prime(x)` function checks if a number is prime by testing divisibility up to the square root of the number. The `factorize(n)` function uses a loop to divide the input number by increasing integers until it finds a factor, then continues dividing the quotient by the same factor until it is no longer divisible. This process is repeated until the quotient is a prime number, which is then added to the list of factors.