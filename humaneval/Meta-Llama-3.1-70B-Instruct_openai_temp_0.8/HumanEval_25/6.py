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
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function works by dividing the input number `n` by the smallest divisor `i` (which starts at 2) and appending `i` to the list of factors as long as `n` is divisible by `i`. The divisor `i` is incremented until it no longer divides `n`, at which point the loop repeats until `n` is reduced to 1. The test cases demonstrate the function's behavior with the examples provided.