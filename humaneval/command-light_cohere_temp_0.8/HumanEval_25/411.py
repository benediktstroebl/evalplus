```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(56)
    [] # Not a prime number, so no factors
    >>> factorize(36)
    [2, 3] # Correct order, but 2 must come before 3
    >>> factorize(48)
    [2, 2, 2]
    >>> factorize(120)
    [2, 2, 3, 3]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    while n % 5 == 0:
        factors.append(5)
        n = n // 5
    while n % 7 == 0:
        factors.append(7)
        n = n // 7
    while n % 11 == 0:
        factors.append(11)
        n = n // 11
    while n % 13 == 0:
        factors.append(13)
        n = n // 13
    while n % 17 == 0:
        factors.append(17)
        n = n // 17
    return factors
``` 
This code defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function first checks if `n` is less than 1 and returns an empty list if so. Then, it starts a loop that iterates through the numbers 2, 3, 5, 7, 11, and 13, and checks if `n` is divisible by each of these numbers. If `n` is divisible, the corresponding factor is appended to the list of prime factors. Finally, the function returns the list of prime factors.