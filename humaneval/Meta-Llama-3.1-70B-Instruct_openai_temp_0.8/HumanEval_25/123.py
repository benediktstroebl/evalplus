```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    i = 2
    factors = []
    
    # Iterate from 2 to sqrt(n)
    while i * i <= n:
        # If i is a factor of n, divide n by i and add i to the list of factors
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    
    # If n is a prime number greater than sqrt(n), add it to the list of factors
    if n > 1:
        factors.append(n)
    
    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of a number. It iterates from 2 to the square root of the number, dividing the number by each divisor it finds. If the number is divisible by the current divisor, it adds the divisor to the list of factors and divides the number by the divisor. This process continues until the number is reduced to 1. If the remaining number is greater than 1, it is a prime number and is added to the list of factors.