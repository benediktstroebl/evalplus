```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
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
    for i in range(3, int(n**0.5), n // i + 1):
        factors.append(i)
        n //= i
    return factors
```

This Python function called **factorize** accepts an integer as input and returns a list of its prime factors, listed in order of decreasing magnitude. The function utilizes a "while" loop to continually divide by 2 until the number becomes odd, at which point all the factors are unique prime factors. 

The output of the function is a list of integers representing the prime factors of the input number.