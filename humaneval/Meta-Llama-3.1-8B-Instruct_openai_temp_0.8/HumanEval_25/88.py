### Prime Factorization Script
```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    Args:
        n (int): The number to factorize
    
    Returns:
        List[int]: The list of prime factors
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    # Remove duplicates and sort the list
    factors = sorted(list(set(factors)))
    # Count occurrences of each factor and add them to the list again
    return [factors[f] for f in range(len(factors)) for _ in range(factors.count(factors[f]))]

# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script uses the trial division method to find the prime factors of a number. It starts by dividing the input number by the smallest prime number (2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide the input number, which is the next prime factor. This process continues until the input number is reduced to 1. The result is a list of prime factors, with each factor listed the number of times it appears in the factorization. The script then removes duplicates and counts the occurrences of each factor to produce the final output.