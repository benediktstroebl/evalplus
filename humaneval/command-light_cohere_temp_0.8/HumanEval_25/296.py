```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    if n > 2:
        factors.append(n)
    return factors
```
This Python function, factorize, takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest, in the format [number of occurrences, factor]. The function uses a while loop to find the prime factors of n, starting from 2. It checks for divisibility by each prime number, starting from 3 up to the square root of n. The function also handles cases where n is a perfect square or a prime number, and returns the list of prime factors accordingly.