```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
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

# Example use cases:
print(factorize(8))    # Output: [2, 2, 2]
print(factorize(25))   # Output: [5, 5]
print(factorize(70))   # Output: [2, 5, 7]
```

This script works by starting at the smallest prime factor (2) and dividing the input number `n` by this factor as long as it's divisible. It then increments the factor until it finds the next number that can divide `n`, which will necessarily be a prime factor. This process continues until `n` is reduced to 1, at which point all of its prime factors have been found. The resulting list of factors is then returned.