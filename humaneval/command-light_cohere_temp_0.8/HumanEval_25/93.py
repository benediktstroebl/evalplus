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
    >>> factorize(55)
    [5, 11]
    >>> factorize(3042)
    [2, 3, 2]
    >>> factorize(1095)
    [5, 23]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    factors.append(n)
    return factors
```
The function factorize in the script above computes the prime factors of the given number n. It does this by following the process:
1. First, it checks if n is even and divides it by 2 if it is even.
2. Next, it iterates through the range of primes starting from 3 up. While the current prime i divides n, it adds i to the list of factors. 

3. Finally, it adds the number n to the list of factors.