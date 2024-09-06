```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    factors.append(int(n))
    return factors

# Example usage
test_factorize = factorize(8)
print(test_factorize)

test_factorize = factorize(25)
print(test_factorize)

test_factorize = factorize(70)
print(test_factorize)
```
This code defines a function called **factorize** that takes an integer as input and returns a list of its prime factors. The function iterates through the prime numbers until the input number is divided by a prime number. The output of the function is a list of numbers, each representing a prime factor of the input number.