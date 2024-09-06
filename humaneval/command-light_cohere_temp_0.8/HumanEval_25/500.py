```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,  while n % i == 0:
        factors.append(i)
        n = n // i
    for num in range(int(n ** 0.5) + 2,  while n % num == 0:
        factors.append(num)
        n = n // num
    factors.append(int('n'))  # Add in case for num = 2
    return factors
```