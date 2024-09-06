```python
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
    >>> factorize(185)
    [5, 7, 13]
    >>> factorize(190)
    [2, 19]
    >>> factorize(196)
    [2, 19, 46]
    >>> factorize(360)
    [2, 2, 3, 3, 20]
    """
    # list of numbers less than n that are factors of n
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            n //= i
    factors.sort()
    common_factors = set(factors)
    # number of common factors
    k = len(common_factors)
    # list of all prime numbers that are less than or equal to n
    primes = []
    for num in range(2, int(n**0.5)+1):
        if num not in common_factors:
            primes.append(num)
    primes.sort()
    prime_factors = []
    for num in primes:
        # find all the factors of n that are equal to num
        for i in range(1, int(n**0.5)+1):
            if n % i == num:
                prime_factors.append(i)
    # remove duplicates
    prime_factors.sort()
    prime_factors.append(n)
    # return factors in order from smallest to largest
    return prime_factors
```