```python
def factorize(n): 
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.

    If number is a product of all factors, the factorization function starts by identifying the first prime factor, which is the smallest integer that is a factor of n.
    """ if n <= 1:
    return []

    # find the smallest prime factor that is a factor of n
    while n % 1 == 0:
        n = n // 1

    # start the loop from the next smallest prime
    p = 2
    while n > 1:
        if n % p == 0:
            break
        n = n // p

    # list all factors
    factors = [p]
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i

    return factors

# pass tests
print(factorize(8))
print(factorize(25))
print(factorize(70))
```