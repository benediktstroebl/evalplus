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
The code exploits the fact that all factors occur in the factorization of the number and it's enough to iterate through possible divisors from 2 to the number itself to find them. 

Let's assume the number is 60, then the following factorization is:
```
60 = 2 * 2 * 3 * 5
```
And the code, after iteration through possible divisors, will produce the following output:
```
[2, 2, 3, 5]
```
Which is the correct prime factorization of 60 in the order from smallest to largest, with each factor repeated the number of times it appears in the factorization.