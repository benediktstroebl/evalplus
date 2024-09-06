```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 2, 5, 5]
    >>> factorize(125)
    [5, 5, 5]
    >>> factorize(NumberKey("abc123"))
    ['a', 'bc', 123]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]
    if n % 2 == 0:
        return [n // 2] + factorize(n // 2)
    factors = []
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        factors.append(factors[-1])
    return factors
``` 
The function factorize is designed to calculate and return a list of prime factors of the given number n, ordered from smallest to largest. It starts with base cases and continues factoring by iterating through numbers up to the square root of n while checking for divisibility. Once the square root is found and the number is not divisible by any smaller prime number, it's considered prime and added to the list of factors.