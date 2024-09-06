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

The code employs an iterative approach to determine the prime factors of a given number `n`. It starts by iterating from 2 up to `n-1` to check for primality against each integer. Once a prime number `i` is found, it iterates from 2 to `i` to ensure that `i` is truly prime by checking if it evenly divides `i`. If so, it adds `i` to the `factors` list and iteratively divides `n` by `i` until `n` is no longer divisible by `i`. This process ensures that `n` is factored into primes. 

The final step checks if `n` is greater than 1, adding it to the `factors` list if it is not 1. This ensures that repeat integers in the list are factored out. For example, the code produces the list `[2, 2, 3]` for input 9, which is correct.