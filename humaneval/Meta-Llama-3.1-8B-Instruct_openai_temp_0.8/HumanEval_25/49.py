```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to be factorized

    Returns:
        List[int]: A list of prime factors of the input number
    """
    i = 2
    result = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            result.append(i)
    if n > 1:
        result.append(n)
    return result

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a simple trial division method to find the prime factors. It starts from the smallest prime number `2` and keeps dividing the input number `n` by the current divisor until `n` is no longer divisible by it. The divisor is then appended to the result list, and `n` is updated to be the remainder of the division. This process continues until `n` is reduced to 1. If `n` is a prime number greater than 1, it is appended to the result list as the last factor. The function returns the list of prime factors in the order from smallest to largest.