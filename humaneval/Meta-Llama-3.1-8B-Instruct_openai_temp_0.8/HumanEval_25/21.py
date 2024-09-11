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
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of the input number `n`. It starts by dividing `n` by 2, then keeps dividing by the smallest divisor possible until it can't anymore, gradually increasing the divisor as it goes. Once it reaches the square root of `n`, it stops and checks whether `n` itself is a prime number (in which case it's a single-element list), returning the list of factors at the end.