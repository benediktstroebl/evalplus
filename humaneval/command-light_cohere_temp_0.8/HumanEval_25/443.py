```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(300)
    [3, 3, 5, 5, 7, 11]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
   
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        n /= i
        factors.append(i)
   
    return factors
```
The function factorizes a given number `n` into a list of its prime factors in a specific order. 

It uses the while loop to keep dividing by primes until the number becomes a prime itself or a number which is less than or equal to the square root of a prime number.