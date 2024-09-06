```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    if not n:
        return []
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    n = n // 2
    for i in range(3, int(n**0.5) + 1, step by step):
        is_prime = True
        counter = 0
        for j in range(2, int(n**0.5) + 1, step by step):
            if n % j == 0:
                is_prime = False
                counter += 1
        if is_prime:
            factors.append(int(counter))
                n = n / int(counter)
    return factors
# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```