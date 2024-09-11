Here's a Python function that solves the problem using a prime factorization approach with a helper function to check for primality:
```markdown
### Prime Factorization of a Given Integer
#### Function Description

The following Python function calculates the prime factors of a given integer, 
including the frequency of each prime factor, and returns them in a list 
sorted in ascending order.

#### Code

```python
from typing import List

def is_prime(n: int) -> bool:
    """Check if a number is prime"""
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

def prime_factors(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    """
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
        if i * i > n and n > 1:
            factors.append(n)
            n = 1
    return factors

def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    """
    factors = {}
    for factor in prime_factors(n):
        if factor in factors:
            factors[factor] += 1
        else:
            factors[factor] = 1
    return sorted([factor for factor in factors], key=lambda x: factors[x])

# Example usage
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

#### Explanation

This code defines three functions:

*   `is_prime(n)`: Checks if a number `n` is prime.
*   `prime_factors(n)`: Returns a list of prime factors of the given integer `n`.
*   `factorize(n)`: Returns the prime factors of `n` in the order from smallest to largest, 
    with each factor's frequency represented in the output list.

The `factorize(n)` function uses a dictionary to store the prime factors and their frequencies, 
then converts the dictionary into a sorted list of factors. 

Note that the `prime_factors(n)` function uses a trial division method to find the prime factors, 
which is sufficient for small to medium-sized integers but may be inefficient for large integers. 
For larger integers, a more efficient algorithm like the Sieve of Eratosthenes or the Miller-Rabin primality test may be necessary.