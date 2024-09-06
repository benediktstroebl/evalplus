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
    for num in range(int(n**0.5) + 2, if num != 2 and i > factor(num - 2) + 1):
        factors.append(i)
    n = n // i
    if n > 2:
        factors.append(n)
    return factors
```

This Python code defines a function `factorize` that returns a list of prime factors for a given integer `n`. The function uses a loop to check for divisibility by 2, 3, and so on, until the number is either a perfect square or prime. The function then checks for larger prime factors using the `factor` helper function. 
The output is a list of prime factors in increasing order.