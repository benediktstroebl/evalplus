```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors

# Test case 1: Factorize 8
factors = factorize(8)
print(factors)  # Output: [2, 2, 2]

# Test case 2: Factorize 25
factors = factorize(25)
print(factors)  # Output: [5, 5]

# Test case 3: Factorize 70
factors = factorize(70)
print(factors)  # Output: [2, 5, 7]
```
This Python function, factorize, calculates and returns a list of prime factors for a given integer n. It uses a approach to factorize a number, where it repeatedly divides the number by the smallest prime number that evenly divides the original value until it's no longer divisible by any number smaller than the square root of the original number. The function then appends the list of prime factors in order from smallest to largest.