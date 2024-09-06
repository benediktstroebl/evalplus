```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which correspond to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(101)
    [2, 3, 5, 7, 11]
    >>> factorize(500)
    [2, 4, 5, 25, 125]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    for i in range(5, int(n**0.5)+1, while n % i == 0:
        factors.append(i)
        n //= i
    return factors
``` 
The function employs a loop that checks divisibility by 2, 3, and the prime numbers starting from 5. Additionally, it utilizes the loop to check for divisibility by individual prime numbers, incrementing the loop by one each time the condition is met. The function also utilizes the condition for each prime number to be factored out.