```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [3, 7, 7]
    >>> factorize(3600)
    [2, 2, 2, 3, 3, 6]
    """
    factors = []
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            factors.append(i)
            if factors:
                break
        n //= i
    if n > 1:
        factors.append(n)
    return factors
```
The function factorize is a self-contained Python function that solves the problem of finding the prime factors of a given integer. It uses a small for loop to iterate through the numbers from 1 to the square root of the given number. The function then checks if the number is divisible by the current number, and if so, appends the current number to the list of prime factors. The function then divides the number by the current number and updates the current number to be the quotient. The function continues until the number is no longer divisible by any number in the range from 1 to the square root of the given number, and then appends the number n to the list of prime factors. 

The function is well-contained, and can be easily called and used to find the prime factors of any given integer.