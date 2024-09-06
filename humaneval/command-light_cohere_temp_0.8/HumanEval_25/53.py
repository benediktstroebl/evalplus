```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,  :
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function first divides n by 2 to get the first prime factor. Then, it iterates through the range of prime numbers to check if n is divisible by them. If n is divisible, it starts checking the next prime number.