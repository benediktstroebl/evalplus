```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
    n (int): The input number to be factorized.
    
    Returns:
    List[int]: A list of prime factors of the input number.
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
    return factors

# Test cases
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This Python script defines a function called `factorize` which calculates the prime factors of a given integer. It iterates through numbers from 2 up to the square root of the input number and checks if the current number is a factor. If it is, the function divides the input number by this factor and adds it to the list of factors. The process continues until the input number is reduced to 1. Any remaining number greater than 1 is a prime factor and is also added to the list. The function returns the list of prime factors.