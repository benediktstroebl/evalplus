```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5) + 1, if n % j == 0:
        factors.append(j)
    n = n // j
    return factors
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of prime factors of `n` in the order of their greatest magnitude. The function uses a same algorithm as the original Python documentation, but it's wrapped in the `factorize` function to be self-contained.