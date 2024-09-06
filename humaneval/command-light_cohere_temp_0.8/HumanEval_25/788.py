```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    Input number should be a positive integer
    """
    if not_positive(n):
        raise ValueError("Input number should be a positive integer.")

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        for i in range(3, int(n**0.5), i += 2):
            factors.append(i)
        n //= i

    return(factors)

def not_positive(n: int) -> bool:
    """ Check if given number is positive
    """
    return n > 0

``` 
The provided Python script defines a function factorize, which calculates and returns a list of prime factors for a given positive integer. It also includes a function to check if a given number is positive or not. The factorize function follows the algorithm to find the prime factors of the input number, ensuring the list is ordered from the smallest to the largest prime factors.