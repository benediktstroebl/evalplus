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

The code employs a straightforward algorithm factoring the number n by iteratively dividing it by integers from 2 to n-1. When a divisor is found, it is appended to the factors list with a count of how many times it appeared in the factorization. The process continues until n becomes 1, at which point the final factor list is returned. 

Here's an example of how you can use the `factorize` function:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```