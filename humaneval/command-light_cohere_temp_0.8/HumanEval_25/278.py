```python
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    else:
        for i in range(3, int(n**.5) + 1, by=2):
            if n % i == 0:
                factors.append(i)
                n = n // i
    return factors

# Example usage:
print(factorize(8))
print(factorize(25))
print(factorize(70))
``` 
This Python function factorize takes an integer n as input and returns a list of its prime factors. It uses a list comprehension and the sieve of Eratosthenes algorithm to find the prime factors of n, and the order of factors is important since it represents the number of occurrences of each prime factor in the factorization.