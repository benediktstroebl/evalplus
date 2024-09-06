```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
``` 
This function, factorize, accepts an integer n and returns a list of its prime factors. It uses a time to efficiently find the smallest prime factor of a given number, and then repeatedly divides the number by the smallest prime factors until the number becomes 1. The prime factors are then listed in order from the smallest to the largest.