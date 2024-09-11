```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    
    :param n: The number to factorize
    :return: A list of prime factors
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
assert factorize(8) == [2, 2, 2]
assert factorize(25) == [5, 5]
assert factorize(70) == [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors in ascending order. The function works by dividing `n` by the smallest prime number (2) as long as it's divisible, then moving on to the next prime number (3), and so on, until `n` is reduced to 1. The factors are appended to the `factors` list as they are found.

The script also includes test cases using Python's built-in `assert` statement to verify that the function works correctly.