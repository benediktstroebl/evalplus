```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    []
    >>> factorize(11)
    []
    """
    m = 0
    for i in range(2, int(n**0.5) + 1):
        while(n%i == 0):
        m += 1
        n //= i
    factors = [m]
    while(n > 1):
        m += 1
        n //= i
        factors.append(m)
    return factors
``` 
This code defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of the number `n` in ascending order. The function first initializes a number of prime factors as `m` and then iterates through the numbers from 2 to the square root of the number. 

Finally, it returns a list of numbers `factors` that are the prime factors of the number `n` in the order from smallest to largest.