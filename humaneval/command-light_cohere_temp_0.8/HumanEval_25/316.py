```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(120)
    [2, 2, 2, 3, 5]
    >>> factorize(500)
    [5, 25, 125]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    factors.append(n)
    if n >= 1 else break
    for i in range(3, int(n**0.5)//1, while n % i == 0:
        n /= i
    factors.append(i)
    return factors
``` 
The function, factorize, takes an integer n as input and returns a list of prime factors of the number in ascending order. The function first divides the factorizes by 2, if n is even, and adds 2 to the list of factors. 

It then iterates through prime factors, starting from 3 up to the square root of n, while dividing n by each prime factor to find its factorization.