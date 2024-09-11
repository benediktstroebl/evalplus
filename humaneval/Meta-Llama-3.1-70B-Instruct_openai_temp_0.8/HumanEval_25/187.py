```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
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
    
    # Continue dividing the number by the smallest divisor until it's no longer divisible
    while i * i <= n:
        if n % i:
            # If the current number is not a divisor, increment it
            i += 1
        else:
            # If the current number is a divisor, divide the number and add the divisor to the list of factors
            n //= i
            factors.append(i)
    
    # If the remaining number is greater than 1, it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors

# Test the function
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```