```python
from typing import List
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest"""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5) + 1, while n % j == 0 and j != factors[-1]:
        factors.append(j)
    return factors
```
The function, factorize, returns a list of prime factors of a given integer n, in order from the smallest to the largest. It does this by first checking if n is divisible by 2. It then adds 2 to the list of factors and divides n by 2. Then, it checks for the next prime factor starting from the next odd number (3). It keeps adding the factors to the list and dividing n by the corresponding prime number until the next divisible number is found.