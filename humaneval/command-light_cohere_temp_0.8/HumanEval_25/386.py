```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization of the number.
    Input number should be equal to the product of all factors
    """
    if n < 2:
        return []
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(n)
    return factors
```
The function factorize is designed to determine the prime factors of a given integer n and return them in order, from the smallest to the largest factor. 

The time complexity of the function is O(sqrt(n)), as it iterates up to the square root of n, checking for divisibility up to the corresponding square root. 

Additionally, it only checks divisibility up to the square root, making it more efficient compared to checking for each prime factor individually.