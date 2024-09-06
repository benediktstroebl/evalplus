```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns list of prime factors of a given integer in descending order. Each of the
    factors should be listed number of times, corresponding to how many times it appears in factorization.
    Input:
    - the number to be factorized.
    """

def is_prime(n: int) -> bool:
    """
    Check if the number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factorize_by_primes(n: int) -> List[int]:
    """
    Factorize a given number using is_prime function
    """
    factors: List[int] = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5), n // = i**2):
        if is_prime(n // i):
            factors.append(i)
    factors.append(n // i**2)
    return factors

# Example:
print(factorize_by_primes(8))  # [2, 2, 2]
print(factorize_by_primes(25))  # [5, 5]
print(factorize_by_primes(70))  # [2, 5, 7]
```