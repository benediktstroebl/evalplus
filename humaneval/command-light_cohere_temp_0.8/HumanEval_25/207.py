```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i
    for num in range(3, int(n**0.25), 
        while num * num + 4 <= n:
            factors.append(num)
    if n % num == 0:
                factors.append(num * 2)
    return factors
```

This function utilizes a loop and testing for divisibility to find the prime factors of a given number. 
It follows the trial and error method and returns the list of prime factors of the given number.