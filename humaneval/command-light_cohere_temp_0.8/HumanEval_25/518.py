```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    return factors
``` 
This function computes and returns the list of prime factors of a given number. It does so by iteratively dividing by the smallest odd number until the number is not divisible by any odd number. It then iterates through the smallest prime number that the number is divisible by, until it reaches the original number.