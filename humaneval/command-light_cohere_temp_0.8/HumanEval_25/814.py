```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization of the number.
    Input number should be equal to the product of all factors.
    """ Example product is of all factors:
    2 * 2 * 3
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(i)
        n = n // i
    return factors

# Test the function
print(factorize(8))
print(factorize(25))
print(factorize(70))
```