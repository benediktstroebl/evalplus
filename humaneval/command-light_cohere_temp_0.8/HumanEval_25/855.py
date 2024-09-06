```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in the order of their corresponding multiplications.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) // n %= 2, i * i):
        factors.append(i)
        n //= i
    for j in range(int(n**0.5) // n %= i, j * j):
        factors.append(j)
        n //= j
    return factors
``` 
This Python function, `factorize`, is designed to determine the prime factors of a given integer `n`. The function iterates through potential prime factors and checks if they divide the `n` evenly. It then lists each factor in the order of their corresponding multiplications, ensuring that the factors are listed correctly. The function takes an integer `n` as input and returns a list of its prime factors.