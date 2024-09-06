```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5, 2)):
        while n % i == 0:
            factors.append(i)
            n = n // i
    return factors

# Test
print(factorize(8))
print(factorize(25))
print(factorize(70))
```