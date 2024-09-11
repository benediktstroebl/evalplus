```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
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
print(factorize(8))   # Expected output: [2, 2, 2]
print(factorize(25))  # Expected output: [5, 5]
print(factorize(70))  # Expected output: [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to divide the input number `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. The divisor `i` is then added to the list of factors, and the process is repeated until `n` is reduced to 1. If `n` is a prime number greater than 1, it is added to the list of factors at the end.