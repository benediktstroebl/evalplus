```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    1. Check for oddness. If the number is odd, divide it by 2 and move to next iteration.
    2. Check for even following factors: If the number is even, check if the square of it is less than sqrt(n). If true, it is divisible by the square of some prime number.
    3. Iterate through All advance prime factors:
    If we got a factor, we add it to the list and make a new factor of that number, which is found by prime factor theorem.
    """
Example:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    for i in range(3, int(n**0.5)+1,):
        if n % i == 0:
            factors.add(i)
            factors.add(i, 1, n // i)
            factors.add(i, n // i)
    if i == int(n**0.5)+1:
        break
    return factors
``` 
This function uses trial and error to find prime factors, which is more efficient than the Sieve of Eratosthenes algorithm.