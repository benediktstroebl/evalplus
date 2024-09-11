```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to factorize

    Returns:
    List[int]: A list of prime factors of the given number
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
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script works by continuously dividing the input number `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. This process is repeated with the next divisor `i+1` until `i*i` is greater than `n`. At this point, if `n` is greater than 1, it means that `n` is a prime number and is added to the list of factors. The function then returns the list of factors.