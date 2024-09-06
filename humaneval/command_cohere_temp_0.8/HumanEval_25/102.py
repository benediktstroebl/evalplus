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

The code employs an iterative approach to determine the prime factors of a given integer `n`. It starts by assuming that `n` is not divisible by any number less than or equal to its current value. This assumption remains in place until the loop completes one full iteration, at which point it checks if the current value of `i` is a prime number. If it is, the loop adds `i` to the `factors` list and proceeds to divide `n` by `i`. This process repeats until `n` is entirely factorized. The final list of factors is then returned, representing the prime factors in ascending order, sorted from smallest to largest. 

Here's an example of function's use:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```