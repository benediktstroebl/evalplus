```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count > 0:
                factors.append(i)
                factors.append(count)
    if n > 1:
        factors.append(n)
        factors.append(1)
    return factors[1:]
```

The factorization algorithm works by iterating through numbers from 2 up to the input number `n` and checking if it can be divided evenly. When a factor is found, the algorithm repeatedly divides `n` by the factor and keeps track of the count using the `count` variable. This loop ensures that the factor is removed from `n` the appropriate number of times. The process continues until `n` is reduced to 1, at which point the factorization is complete. Finally, the function returns a list of prime factors, where each factor is followed by its corresponding count.