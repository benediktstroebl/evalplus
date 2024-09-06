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

    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % (i * i) == 0:
                n //= i
                factors.append(i)
                i += 1
        else:
            i += 2

    if n > 2:
        factors.append(n)

    return factors

``` 
This code defines a function called `factorize` that takes an integer n as input and returns a list of its prime factors in descending order. It uses a method of trial and error by adding numbers until the number can't be divided by any smaller number without remaining a remainder.  The loop starts from 2 and adds numbers until the square of the number is greater than the original number.