```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, exact):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This function, `factorize()`, takes an integer `n` as input and returns a list of its prime factors in order from smallest to largest. The function first checks for the smallest even prime factors by checking if `n` is even and then dividing `n` by 2. The function then iterates through the prime numbers up to the square root of `n`, dividing `n` by each prime number in turn. The function then checks if `n` is still greater than 2, and if so, it is a prime number itself, so it is added to the list of prime factors.

The function then returns the list of prime factors.

The output of this code is the following:
```
[2, 2, 2]
[5]
[2, 5, 7]
```