```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, ]:
        while n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)  # last factor (if it's even)
    return factors

# Test cases
print(factorize(8)) # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This Python code defines a function called factorize that calculates and returns a list of prime factors for a given integer n. The function uses a approach to factorize the number, which involves checking for divisibility with the odd numbers up to the square root of n, while discarding even numbers. The function then appends each found factor to the factors list. The code also includes test cases that demonstrate the functionality of the factorize function with different input values.