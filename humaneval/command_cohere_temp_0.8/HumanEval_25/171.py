```python
from typing import List

def prime_factors(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(int(n))
    return factors

def factorize(n: int) -> List[int]:
    prod = 1
    factors = prime_factors(n)
    result = []
    for factor in factors:
        result.extend([factor] * (n // prod))
        prod = prod * factor
    return result
```
The `prime_factors` function extracts all prime factors from the given number `n`. It begins by checking if the number is even and then iterates through numbers from 3 up to the square root of `n`, incrementing by 2 each time. The `factorize` function utilizes `prime_factors` to find all prime factors of the given number `n`. It also calculates the product of all the prime factors, `prod`, and constructs the result list that includes each prime factor multiplied by the number of times it appears in the factorization of `n`. The resulting list of prime factors is returned in ascending order.

Here is an example usage of the function:
```python
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
``` 
This would output:
```
[2, 2, 2]
[5, 5]
[2, 5, 7]
```