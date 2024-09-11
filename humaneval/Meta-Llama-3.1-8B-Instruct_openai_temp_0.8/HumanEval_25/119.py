### Prime Factorization of an Integer
Here is a Python script that uses a simple algorithm to factorize an integer into its prime factors:
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Parameters:
    n (int): Input number to be factorized.
    
    Returns:
    List[int]: A list of prime factors.
    
    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 2, 5, 7]
    """
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    
    return factors
```
This script works by dividing the input number `n` by the smallest prime divisor (2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`. This process continues until `n` is reduced to 1.

You can test this function with different inputs to see the prime factorization of those numbers.