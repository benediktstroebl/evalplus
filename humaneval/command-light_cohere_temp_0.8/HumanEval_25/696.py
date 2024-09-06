```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in the factorization
    Input number should be a positive integer
    """
    if n <= 1:
        return []
    
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
```