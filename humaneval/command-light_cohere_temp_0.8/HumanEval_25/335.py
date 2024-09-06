```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Sieve of Eratost method is used to find prime factors.
    >>> factorize(8)
    [2, 2]
    >>> factorize(25)
    [5]
    >>> factorize(70)
    [2, 5, 7]
    """
    prime = []
    is_prime = [True] * (n + 1)
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
        for j in range(i*2, int(n**0.5)+1,
            if is_prime[j]:
                is_prime[j] = False
    for j in range(len(is_prime)):
        if is_prime[j]:
            prime.append(j)
    return prime
```