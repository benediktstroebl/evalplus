```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(81)
    [] # Not a prime number
    >>> factorize(9)
    [] # Not a prime number
    """
    # The purpose of this function is to return a list of prime factors of a given integer in descending order.
    factors = []
    for num in range(2, int(n**0.5)+1): 
        while num*num > n: 
             break
        while n % num == 0:
            factors.append(num)
            n = n//num
    return factors
```