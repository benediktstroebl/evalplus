```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the prime factors are listed number of times corresponding to how many times it appears in factorization of the given number.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(1000)
    [2, 2, 2, 5, 5, 7, 11, 53]
    """
    # Check if n is 1 or divisible by 1
    if n <= 1:
        return [n]

    # Find factors of n
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n // 2
    while n % 3 == 0:
        factors.append(3)
        n // 3
    for i in range(5, int(n**0.5)//1):
        factors.append(i)

    # Identify all prime factors
    prime_factors = []
    for i in range(len(factors)):
        if factors[i] > 1 and factors[i] <= n:
            prime_factors.append(factors[i])

    # Reverse the list and return
    return prime_factors[::-1]
```