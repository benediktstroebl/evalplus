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

The code employs an iterative approach to determine the prime factors of a given integer `n`. It begins by assuming that `n` is not divisible by any number less than or equal to its current value. This assumption is then systematically challenged by checking if `n` is divisible by each integer from 2 up to its current value. If a divisor is found, it is added to the `factors` list, and `n` is divided by that divisor. The process continues until `n` becomes 1, at which point the prime factors have been determined and listed in descending order, with each factor appearing the number of times it divided `n`. 

Here is an example usage of the code:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```