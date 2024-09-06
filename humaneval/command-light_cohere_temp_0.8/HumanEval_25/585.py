```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    return factors
```

This function starts by checking for divisibility by 2 and appending 2 to the list of factors. It then iterates through the numbers from 3 to the square root of n, while keeping track of factors. This process continues until the important prime factors are found, at which point, all subsequent factors for n will be multiples of its corresponding factor.