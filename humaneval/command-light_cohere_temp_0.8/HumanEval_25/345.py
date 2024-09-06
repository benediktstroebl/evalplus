```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeases in factorization.
    Input number should be a integer
    """
    if n < 2:
        return []
    if n % 2 == 0:
        return [2]
    for i in range(3, int(n**0.5/5, while n % i == 0):
        if n % (i+2) == 0:
            return [i, i+2] + factorize(n//(i+2))
    return []
```