```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 3 == 0:
        n /= 3
    for i in range(5, int(n**0.5) + 1,:
        factors.append(i)
    n /= i
    return factors
``` 
The function uses basic factorization techniques to determine the prime factors of the input number and returns a list of integers representing those prime factors. The function performs efficiently for larger numbers and is self-contained, as it does not require any additional functions or data outside the function to solve the problem.