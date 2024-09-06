```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in the factorization
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    []
    >>> factorize(55)
    [5, 11]
    """
    factors = []
    while n > 1:
        b = int(sqrt(n) + 1) // 2
        if n % b == 0:
            factors.append(b)
            n //= b
    factors.append(n)
    return factors
``` 
This Python code defines a function called `factorize` that calculates and returns a list of prime factors for a given integer `n`. It iterates through the numbers and checks if the number is divisible by any odd prime number, starting from 2. If a number is divisible by an odd prime number, it adds that prime number to the list of factors. The code then handles the big O/O notation, so you can easily extend the function to work with larger numbers without running into the code.