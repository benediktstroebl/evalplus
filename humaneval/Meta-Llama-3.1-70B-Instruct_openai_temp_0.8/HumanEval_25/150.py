```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
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
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script works by dividing the input number `n` by the smallest prime factor `i` as long as it's divisible. The divisor `i` is then appended to the list of factors. This process continues until `n` is reduced to 1, at which point all its prime factors have been found. The last factor is appended to the list only if `n` is greater than 1 to avoid appending 1 to the list.

Note that this algorithm has a time complexity of O(√n) which makes it efficient for large inputs.