```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    :param n: Input number
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

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function works by dividing the input number `n` by the smallest divisor `i` (starting from 2) until `n` is no longer divisible by `i`. Then, it increments `i` and repeats the process until `i` is greater than the square root of `n`. If `n` is greater than 1 at the end of the loop, it means that `n` is a prime number and is added to the list of factors.

The test cases at the end of the script demonstrate the function's behavior with different inputs.