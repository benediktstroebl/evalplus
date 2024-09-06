```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many times it appears in the factorization of the number.
    Input number should be equal to the product of all factors."""
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(2)
   
    while n > 1:
        is_prime = True
        for num in factors:
            if n % num == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(n)
            n = n / num
    return factors
# Example usage
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```