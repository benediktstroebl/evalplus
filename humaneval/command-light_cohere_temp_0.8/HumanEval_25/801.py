```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```

This function takes an integer n as input and returns a list of prime factors of n, in order from smallest to largest. It uses a ** while loop to find factors and checks divisibility by all numbers from 3 to the square root of n. The function also handles cases where n is greater than 2 correctly.