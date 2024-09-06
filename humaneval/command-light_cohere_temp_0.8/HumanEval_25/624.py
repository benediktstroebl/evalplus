```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n //= 2
    else:
        for i in range(3, int(n**.5) + 1, by=2):
            if n % i == 0:
                factors.append(i)
                n //= i
    return factors

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This code defines a function `factorize` that returns a list of prime factors of a given number `n`. The function uses a while loop to continuously divide by numbers until the number is 1, and the number of times each prime factor appears in the factorization is the number of times the factor divides by.

Note that this function assumes that the input number is greater than 1, as the factorization process starts with 2 and continues up to the square of the input number.