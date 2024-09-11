```python
from typing import List


def factorize(n: int) -> List[int]:
    """ 
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
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
if __name__ == "__main__":
    print(factorize(8))  # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of the input number `n`. The loop starts from 2 and checks whether the current number is a factor of `n`. If it is, the number `n` is divided by the current factor and the factor is added to the list of factors. This process continues until `n` is reduced to 1. If at any point `n` is not divisible by the current factor, the next number is checked.