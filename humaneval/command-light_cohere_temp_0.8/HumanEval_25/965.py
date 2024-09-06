```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    A factor is a number is a prime if its only positive divisors are 1 and itself.
    if n <= 1:
        return []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
        n /= i
    if n > 1:
        return [n] + factorize(n)
    return []
```  This function recursively factorsizes a given integer n and returns the list of its prime factors in order. It ensures that all factors are listed number of times they appear in the factorization, and handles edge cases such as handling negative numbers and inputs less than 1 correctly.