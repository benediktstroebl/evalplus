```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    :param n: Input integer to be factorized
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


# Example usage:
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in ascending order. The function iterates over possible factors from 2 to the square root of `n`, dividing `n` by each factor as many times as possible and appending the factor to the result list. Finally, if `n` is greater than 1 (i.e., it has not been fully factorized), it is appended to the result list as a prime factor. The script includes example usage of the function.