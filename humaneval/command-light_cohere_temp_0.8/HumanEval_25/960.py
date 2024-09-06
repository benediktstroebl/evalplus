```python
from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    return factors
``` 
This script defines a function factorize that takes an integer n as input and returns a list of its prime factors. The function first adds the factor of 2 to the list if n is even, then iterates through the odd prime numbers up to the square root of n, adding each one as a factor if n is divisible by the corresponding number.