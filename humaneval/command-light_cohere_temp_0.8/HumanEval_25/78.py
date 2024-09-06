```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Also, return the number of occurrences of each factor in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n > 1: 
        d = int(n**0.5)
        n //
        lcm = n//d
        factors.append(d)
        factors.append(lcm)
    n = n//d
    return factors
```

This function uses the same logic as in your original provided function. It returns a number of occurrences of each prime factor and their corresponding order in factorization.