```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    """
    def is_prime(n: int) -> bool:
        """ Checks if the given number is prime"""
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
    
    factors = []
    while n > 0:
        if is_prime(n):
            factors.append(n)
        n = n //ulo(2) 
    return factors
``` 
The function checks if a number is prime and then proceeds to the factorization process.