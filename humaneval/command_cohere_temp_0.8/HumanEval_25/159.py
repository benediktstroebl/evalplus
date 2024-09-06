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

The code uses a simple algorithm to find the prime factors of an integer `n`. It iterates through numbers from 2 up to `n` and checks if each number is prime using a nested loop. If a number is prime, it is added to the `factors` list and the algorithm repeatedly divides `n` by that prime until `n` is fully factorized. The resulting list of prime factors is returned in ascending order. 

To test this function, you can use the following inputs and compare the results with the expected output:
```python
>>> factorize(8)
[2, 2, 2]
>>> factorize(25)
[5, 5]
>>> factorize(70)
[2, 5, 7]
```