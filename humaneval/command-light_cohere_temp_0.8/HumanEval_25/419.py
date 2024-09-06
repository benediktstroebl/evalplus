```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Calculate the prime factors
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    while n % 5 == 0:
        factors.append(5)
        n //= 5
    while n % 7 == 0:
        factors.append(7)
        n //= 7
    for num in factors:
        while n % num == 0:
            factors.append(num) * n //= num
    return factors
``` 
This code defines a function called factorize that takes an integer n as input and returns a list of its prime factors. The function first divides n by 2 and adds 2 to the list of factors. Then it divides n by 3 and adds 3 to the list of factors. Finally, it divides n by 5 and adds 5 to the list of factors. The function then checks if n is divisible by each prime number up to the current factor, and adds the corresponding prime number to the list of factors.