```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The number to factorize
    :return: A list of prime factors
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
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors. The function iterates from 2 to the square root of `n`, checking if `n` is divisible by the current number `i`. If it is, `n` is divided by `i` and `i` is added to the list of factors. If `n` is not divisible by `i`, `i` is incremented by 1. This process continues until `n` is reduced to 1. If `n` is greater than 1 at the end of the loop, it means `n` is a prime number and it is added to the list of factors. The function then returns the list of factors.