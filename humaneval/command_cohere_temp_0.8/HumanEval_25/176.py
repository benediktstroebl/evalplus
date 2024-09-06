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

The code employs an iterative approach to determine the prime factors of a given number `n`. It begins by assuming that `n` is not divisible by any number less than or equal to its current value. This assumption is then repeatedly tested for each integer up to  `i`  . If  `i`  is found to be a factor, it is added to the list of  `factors`  , and the loop continues until all divisors are extracted. The loop is designed to stop when the remaining number is 1, as numbers greater than 1 are by definition not prime. As a result, the function returns a list containing each distinct prime factor, with each factor repeated according to its multiplicity in the factorization of the original number.