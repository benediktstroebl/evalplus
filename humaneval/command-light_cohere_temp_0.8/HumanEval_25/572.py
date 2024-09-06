```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all the factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    []
    >>> factorize(11)
    []
    >>> factorize(9)
    []
    """
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
``` 
The function uses a for loop to iterate through factors from 2 up until the input number is divisible by the current factor. The function then returns a list of prime factors, with each factor listed number of times it appears in the factorization.