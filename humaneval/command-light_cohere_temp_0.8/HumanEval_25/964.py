```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be number of times corrresponding to how many times it appears in factorization.
    """
    basic factors first and then the number is prime"""
    if n <= 1:
        return [n]
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)
    continue
    for i in range(3, int(n**0.5) + 1, by 5):
        if n % i == 0:
            factors.append(i)
            n //= i
    factors.append(int(n))
    return factors

# Example usage:
print(factorize(8))
print(factorize(25))
print(factorize(70))
```