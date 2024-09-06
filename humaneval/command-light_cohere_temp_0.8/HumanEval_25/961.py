```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest.
    sieve_of_erat : This is a simple method using Sieve of Eratosthenes to find prime factors.
    This for a method uses below formula : ps < p1+p2+....+pm
    where ps = prime factor sum, p1, p2, ..., pm are prime factors.
    """ return [ps/n
    [ps]
    """
    # create a list of all numbers from 2 to n
    lis = [i for i in range(2, n+1)]
    # find prime numbers using Sieve of Eratosthenes
    # one less than i will become 0
    # so we can ignore that number
    for i in range(3, int(n**0.5) + 1):
        lis[i] = 0
    for p in range(2, int(n**0.5)):
        # if lis[p] == 0:
            # p is a prime number, mark all multiples of p as non-prime
            for i in range(p*p, n+1, p*p):
                lis[i] = 0
    # print the list of prime factors in the order of increasing number
    factors = []
    for i in lis:
        if i != 0:
            factors.append(i)
    # add number of occurrences
    factors.append(lenum(i))
    return factors
```