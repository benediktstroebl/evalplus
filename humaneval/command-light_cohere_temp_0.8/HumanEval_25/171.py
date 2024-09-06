```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    if n < 1: return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5 / 2, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.5 / 2, 2**):
        if n % (j*j) == 0 and j != int(n**0.5 / 2):
            factors.append(j)
    if j != factors[-1]: factors.append(j)
    return factors
```
This function takes an integer n as input and returns a list of prime factors of the given number, in ascending order. It starts with 1 and checks for 2 (since 2 is the only even prime factor), then iterates through numbers 3 to <sqrt(n)**, checking for divisibility with each prime factor. It continues with each prime factor until it starts to become ineffective or larger than sqrt(n).  Finally, it checks if n is a perfect square and returns the last prime factor accordingly.