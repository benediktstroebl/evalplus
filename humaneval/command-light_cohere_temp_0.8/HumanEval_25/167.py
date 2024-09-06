```python
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(90)
    []
    >>> factorize(9)
    []
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == False:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    factors = []
    for i in range(2, n + 1):
        if sieve[i] == True:
            factors.append(i)
    return factors
```

The function `factorize` takes an integer `n` as input and returns a list of its prime factors in order of size from smallest to largest. It uses the efficient algorithm called Sieve of Eratosthenes to find the prime factors. 

You can use this code to solve the problem of finding the prime factors of any given number.