```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which corresponds to the frequency of the factor in factorization
    Input number should be a product of its factors
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
   
    for i in range(3, int(n**0.5) // n // 2, 4, 6, 8, ...):
        if n % i == 0:
            factors.append(i)
            n /= i
    return factors

# Example Test Cases:
print(factorize(8))
print(factorize(25))
print(factorize(70))
 ```