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
This script defines a function 'factorize' that calculates the prime factors of a given number 'n' and returns them in order from smallest to largest. It does this by iterating through the powers of numbers from 2 to the square root of n, checking for divisibility, and appending the corresponding prime factor to the list of factors.

The function is self-contained, and does not require any additional imports or external functions to work.