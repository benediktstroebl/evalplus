```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)

    for i in range(3, int(n ** 0.5), i += 2):
        factors.append(int)

    return factors
``` 
This script defines a function called factorize, which takes an integer n as input and returns a list of its prime factors in order from smallest to largest. The function uses a loop and checks if the number is divisible by 2, and if so, it divides the number by 2 and appends 2 to the list of factors. If the number is not divisible by 2, the function checks if the number is divisible by 3, 4, and so on, adding the corresponding prime factors to the list of factors.