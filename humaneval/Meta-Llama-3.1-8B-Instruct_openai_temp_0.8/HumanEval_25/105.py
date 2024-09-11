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

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This function uses trial division to find the prime factors of a given integer `n`. It starts by checking if `n` is divisible by the smallest prime number, which is `2`. If it is, it divides `n` by `2` and adds `2` to the list of factors. It continues to do this until `n` is no longer divisible by `2`. Then it moves on to the next prime number, which is `3`, and repeats the process. This continues until `n` is reduced to `1`, at which point the function returns the list of factors.

This function has a time complexity of O(sqrt(n)), where n is the input number, because it only needs to check up to the square root of n to find all prime factors.