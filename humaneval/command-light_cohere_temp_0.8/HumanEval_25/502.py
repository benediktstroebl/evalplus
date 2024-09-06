```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in factorization order corresponding to its corresponding occurrence.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(170)
    [2, 17, 17]
    >>> factorize(100)
    [2, 2, 5, 5, 5]
    >>> factorize(350)
    [2, 2, 5, 7, 5]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), i+ 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(2, int(n**0.5)// j + 1):
        while n % j == 0:
            factors.append(j)
            n = n // j
    factors.append(n)
    return factors
```

This Python script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors of `n`, ordered from smallest to largest. The function first determines if `n` is less than or equal to 1 and returns an empty list. It then enters a prime factorization loop, where it repeatedly divides `n` by the smallest prime number that evenly divides `n`. The smallest prime factor is always the first number in the list. The loop continues by checking divisibility with increasing prime numbers until a factor is found. The function then appends the corresponding prime factor to the list of factors. 

Please note that this solution assumes the input `n` is an integer greater than 1.