```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, halve = i // 2:
        while n % halve == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function takes an integer n and returns a list of its prime factors in descending order. The function first checks for the factor of 2 and adds it to the list. Then it checks for all even prime factors starting from 3 up until the square root of n is reached, and adds them to the list. It then returns the list of prime factors of n.