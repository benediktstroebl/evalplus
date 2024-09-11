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
        List[int]: A list of prime factors
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
print(factorize(100))  # [2, 2, 5, 5]

```
This script defines the `factorize` function, which takes an integer `n` as input and returns a list of its prime factors. The function uses a while loop to iterate over all numbers from 2 to the square root of `n`. If `n` is divisible by the current number `i`, it divides `n` by `i` and adds `i` to the list of factors. If `n` is not divisible by `i`, it increments `i` by 1. Finally, if `n` is greater than 1 at the end of the loop, it means that `n` is a prime number and is added to the list of factors. The function returns the list of factors.