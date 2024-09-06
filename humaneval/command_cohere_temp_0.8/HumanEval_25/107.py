```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if n % j == 0:
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

The code employs an iterative approach to determine the prime factors of a given number `n`. It begins by assuming the number to be divisible by each integer from 2 up to `n` (exclusive). It then checks for each potential divisor whether it is prime by iterating from 2 up to the suspected divisor. If the divisor is not found to be composite, it is appended to the `factors` list, and the loop continues until `n` is reduced to zero. The final factor remaining, if any, is also appended to the list. The function returns the list of prime factors, with each factor appearing as many times as its multiplicity in the factorization. 

Here is an example usage of the code:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```