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

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that finds the prime factors of a given integer `n`. The function uses a simple trial division method to find the factors. It starts with the smallest prime number (2) and keeps dividing the input number `n` until it's no longer divisible. Then it increments the divisor until it finds the next number that can divide `n`. This process continues until `n` is reduced to 1.

The function returns a list of prime factors in the order from smallest to largest, with each factor listed the number of times it appears in the factorization. If the input number `n` is a prime number itself, it will be included in the list of factors.

The script also includes test cases to verify the correctness of the function.