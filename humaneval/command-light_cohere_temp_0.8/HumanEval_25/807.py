```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
The function 'factorize' in this code takes an integer 'n' as input and uses a basic method to locate the prime factors of 'n' to return a list of those factors. It also handles the other edge cases, such as handling the case when 'n' is a prime number, and another edge case, it handles the case when 'n' is a product of two prime numbers.