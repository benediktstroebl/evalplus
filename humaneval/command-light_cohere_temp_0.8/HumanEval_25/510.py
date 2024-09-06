```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [3, 7, 7]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 5]
    >>> factorize(101)
    [2, 3, 5, 101]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2):
        factors.append(i)
    return factors
``` 
This Python function called `factorize` takes an integer `n` as input and returns a list of its prime factors. The function first checks if `n` is less than or equal to 1 and returns an empty list in that case. Then, it iterates through pairs of even numbers until it finds a factor, then it appends that factor to the list of prime factors and keeps on dividing by that factor until it cannot divide the number anymore.  The function also checks if the input number is a prime number and returns the list of its only prime factors.