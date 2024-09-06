```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    for num in factors:
        if num > 1:
            factors.append(factors[num])
    return factors
```
This function, `factorize`, takes an integer `n` as input and returns a list of prime factors of `n` in descending order, along with the count of each factor. The function uses a loop to find factors of the number and the list is built accordingly.