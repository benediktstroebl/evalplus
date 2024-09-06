```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    """
Assume the input is a product of all prime factors.
    For example, 8 = 2 * 2 * 2, 25 = 5 * 5, 70 = 2 * 5 * 7.
    """
    list of prime factors = []
    for num in range(2, int(n**0.5) + 1):
        while num* remained > n:
            if n % num == 0:
                prime_factors.append(num)
                n = n // num
    return prime_factors

# Example
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```