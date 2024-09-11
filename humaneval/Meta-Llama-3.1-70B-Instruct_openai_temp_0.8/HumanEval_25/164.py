```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: Integer to be factorized
    :return: List of prime factors
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

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors. The function iterates from 2 to the square root of `n`, dividing `n` by each number `i` that divides it evenly and adding `i` to the list of factors. If `n` is greater than 1 at the end of the loop, it means that `n` itself is a prime factor, so it is added to the list. The function returns the list of factors.

The test cases at the end of the script demonstrate the function's correctness.