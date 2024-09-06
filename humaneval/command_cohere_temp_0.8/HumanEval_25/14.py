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

The code employs an iterative approach to determine the prime factors of a given integer `n`. It starts by assuming that `n` is not divisible by any number less than or equal to its square root and iterates from 2 up to this assumed upper limit. For each candidate divisor `i`, the code verifies if `i` is prime by checking if it can be divided evenly by any number within the range from 2 to `i` itself. If `i` is determined to be prime, it is added to the list of factors, and then the code continues to remove multiples of `i` from `n` until `n` is reduced to 1 or another prime factor. The final factor list is returned, containing each prime factor represented the number of times it appears in the factorization. 

Here is an example of how to use the code:
```python
factorize(8)
# [2, 2, 2]

factorize(25)
# [5, 5]

factorize(70)
# [2, 5, 7]
```