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
    # list of factors. First find all the Palindrome of the first number of the number.
    factors = []
    def is_prime(num: int) -> bool:
        """Check whether the number is prime or not. 
        If num is 0, 1, or a perfect square, return False
        Otherwise, check whether the number is divisible by all numbers in primes(2, 3, 5, 7, 11, 13, ...)
        until i doesn't divide num by any prime, then i is a factor of num, 
        return True.  otherwise if all prime numbers don't divide num"""
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    # Loop through factors
    for i in range(1, int(n ** 0.5) + 1):
        if is_prime(i):
            factors.append(i)
            factors.append(factors.count(i))
    def factors_count(n: int) -> int:
        """ Return the count of each prime factor in factorization of given number. 

        This function only works with positive integers"""
        result = 0
        for i in range(len(factors)):
            result += factors[i] * factors.count(i)
        return result
    # Return the list of prime factors
    return factors
```