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
        i += 2
    for j in range(3, int(n**0.5) + 1,  while n % j == 0 and j != int(n**0.5):
        factors.append(j)
        n //= j
    return factors
```

The function `factorize` takes an integer `n` as input and returns a list of prime factors of the number `n` in the order from smallest to largest. It uses a method of trial and backtracking to find the prime factors. The function first adds 2 to the list of factors if `n` is even, then it starts looking for the next prime factor to add to the list. The process continues until it finds all prime factors of the number.