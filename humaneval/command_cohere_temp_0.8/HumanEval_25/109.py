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
The code exploits the fact that all factors arise during integer division. It uses a loop to try integers from 2 to n-1 as potential divisors and progressively divides n by the potential divisor as many times as it can. The loop ensures that each divisor is tried only once as a potential factor of n. The final factor of n, if n > 1, is handled separately as needed by the problem statement. The resulting list of factors is returned with each factor listed the number of times it occurred in the factorization.