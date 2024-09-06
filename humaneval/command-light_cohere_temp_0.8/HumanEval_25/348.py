```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    sieve_of_erat: method that returns True if n is divisible by any number less than or equal to it"""

    def sieve_of_er(num):
        primes = [2]
        for i in range(3,int(num**0.75)+1):
            if(num%i==0):
                primes.append(i)
        return primes
   

    factors = []
    for p in primes:
        while n % p == 0:
            n //=p

    for i in range(2,int(n**0.25)+1):
        if n % i == 0:
            factors.append(i)

    return factors
```
This function, `factorize`, uses the Sieve of Eratosthenes to list the prime factors of the given number in descending order.

It first defines the Sieve of Eratosthenes, then generates a list of primes, then loops through those primes to remove multiples of those primes from the given number. 
Finally, it loops through the last odd numbers to check for and add their to the list of prime factors.