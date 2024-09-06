```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.append(n)
    return factors
```

The code employs an iterative approach to determine the prime factors of a given integer `n`. It starts by iterating from 2 up to the given number `n`. For each number, it checks if it is prime by iterating from 2 up to the candidate factor itself. If the candidate factor is prime, it is added to the `factors` list and the remaining factor `n` is divided by it. This process continues until `n` is reduced to 1, at which point the final factor is identified and added to the list. The function returns the list of prime factors, ensuring that each factor is listed the number of times it appears in the factorization.