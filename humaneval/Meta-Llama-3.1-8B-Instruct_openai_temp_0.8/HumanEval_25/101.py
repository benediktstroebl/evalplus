```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to be factorized.

    Returns:
    List[int]: A list of prime factors of the given integer.
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

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. It uses a while loop to iterate from 2 to the square root of `n`, and for each number `i` that divides `n`, it divides `n` by `i` and adds `i` to the list of factors. If `n` is a prime number greater than 1, it is also added to the list of factors. The function returns the list of factors.

The test cases at the end of the script demonstrate the function's behavior with different inputs.