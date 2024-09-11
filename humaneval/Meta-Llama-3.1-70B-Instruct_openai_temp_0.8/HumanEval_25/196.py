```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors

    :param n: The input integer
    :return: A list of prime factors
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

This script uses a simple trial division method to find all the prime factors of a given number `n`. It starts by dividing `n` by the smallest prime number (2), and then continues to divide by increasing integers until it finds a factor. When a factor is found, it is appended to the list of factors and `n` is divided by that factor. This process continues until `n` is reduced to 1. The final list of factors is then returned. If `n` itself is a prime number greater than 1, it is appended to the list of factors at the end.