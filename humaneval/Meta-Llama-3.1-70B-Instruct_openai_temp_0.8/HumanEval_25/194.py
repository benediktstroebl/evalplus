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
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors


# Example usage
if __name__ == "__main__":
    print(factorize(8))   # [2, 2, 2]
    print(factorize(25))  # [5, 5]
    print(factorize(70))  # [2, 5, 7]
    print(factorize(100)) # [2, 2, 5, 5]
```
This script defines a function `factorize(n)` that returns a list of prime factors of the given integer `n`. The function works by dividing the input number `n` by the smallest divisor (starting from 2) until it's no longer divisible. The divisor is then added to the list of factors, and the process continues until `n` is reduced to 1. The resulting list of factors is returned in the order from smallest to largest, with each factor listed the number of times it appears in the factorization.