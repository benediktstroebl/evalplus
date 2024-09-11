```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    :param n: Input integer
    :return: List of prime factors
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
print(factorize(8))    # [2, 2, 2]
print(factorize(25))   # [5, 5]
print(factorize(70))   # [2, 5, 7]
print(factorize(100))  # [2, 2, 5, 5]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of prime factors of `n` in ascending order. The function works by dividing the input number `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. The divisor `i` is then added to the list of factors, and the process is repeated with the next smallest divisor until `n` has been fully factorized.