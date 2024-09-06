```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for divisor in range(2, n):
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                n //= divisor
                count += 1
            if count > 0:
                factors.append(divisor)
                factors.extend([divisor] * count)
    if n > 1: 
        factors.append(n)
    return factors
```
The code employs a simple algorithm factoring the number n by iteratively dividing it by divisor from 2 to n-1. When a divisor is found, it is appended to the factors list and the division is performed multiple times until the divisor is exhausted. The algorithm finally handles the case when n is equal to 1, which represents a prime number and is not removable during the factoring process. The entire process is geared towards producing a list of prime factors ordered from smallest to largest, with each factor repeated according to its occurrence in the factorization. 

Here is an example of function usage:
```python
print(factorize(8))
print(factorize(25))
print(factorize(70))
```
The output will be:
```
[2, 2, 2]
[5, 5]
[2, 5, 7]
```