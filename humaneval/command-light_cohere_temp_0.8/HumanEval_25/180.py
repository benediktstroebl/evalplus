```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to the number of its occurrences in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    []
    """
    if n <= 1:
        return []

    prime = []
    while n % 2 == 0:
        n //= 2
        prime.append(2)
   
    for i in range(3, int(n ** 0.5) + 1,  :
        while n % i == 0:
            n //= i
        prime.append(i)
   
    return prime
``` 
This Python function, factorize, calculates the prime factors of a given integer n. It uses a efficient method that starts with small primes and gradually incorporates larger primes until the original number cannot be divided further. The result is a list of prime factors, where each factor is listed the number of times it occurs in the factorization. 

Finally, it handles edge cases, such as when the input number is 1 or an even number less than 2, returning an empty list.