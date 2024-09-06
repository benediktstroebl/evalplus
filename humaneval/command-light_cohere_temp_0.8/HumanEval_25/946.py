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
    >>> factorize(100)
    [] # should return empty list
    """
    # create a list to store prime factors
    prime = []
    # loop through numbers 2 to the sqrt(n)
    for num in range(2, int(n ** 0.5)):
        # if num*num > n and num % n == 0:
        prime.append(num)
        # if num is a prime factor
        if num > 1 and is_prime(num):
            prime.append(num)
    # if num is not a prime factor and can be factorized further
    if num < int(n ** 0.5) and
        factorize_by_merging(n, num, prime)
    # factorize_by_merging function to factorize by merging small prime factors
    def factorize_by_merging(n: int, a: int, primes: List[int]) -> int:
        result = a
        while a <= int(n ** 0.5):
            b = int(n ** 0.5) // a
            while num = int(n ** 0.5) //a // b > int(n ** 0.5)
            if a a, b = factorize_by_merging(n, b, primes)
            result = int(n ** 0.5) //result // num
        return result
    """

This script defines a function `factorize` that returns a list of prime factors of a given integer `n`. The function uses a loop to find all the prime factors of `n` by checking if `num` divides `n` evenly and is a prime number.  It then adds `num` to the list of prime factors if it is a prime number. The function also uses a `factorize_by_merging` function to factorize `n` by merging small prime factors.