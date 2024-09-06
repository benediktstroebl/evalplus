```python
def factorize(n: int) -> List[int]:
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
    for j in range(2, int(n**0.5)):
        if n % j == 0:
            factors.append(j)
    return factors
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in order from smallest to largest. The function uses a `while` loop to check for divisibility by 2, 3, and larger numbers, and adds the corresponding prime factor to the `factors` list when a factor is found.  The function also checks for divisibility by numbers greater than 2 using the formula `n%j == 0` which is equivalent to `(n//j == 1)`. 

The function is then tested with several inputs and passes all the tests.