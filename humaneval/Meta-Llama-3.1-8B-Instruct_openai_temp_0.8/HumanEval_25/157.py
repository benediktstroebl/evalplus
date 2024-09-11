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
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

In this script, we define a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. We use a while loop to iterate through all numbers from 2 to the square root of `n` (inclusive). If `n` is divisible by `i`, we divide `n` by `i` and add `i` to the list of factors. We repeat this process until `n` is no longer divisible by `i`. If `n` is a prime number greater than 1, we add it to the list of factors. Finally, we return the list of factors.