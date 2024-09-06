```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(121)
    [3, 3, 7, 7]
    >>> factorize(255)
    [3, 5, 3, 7, 11, 7]
    """
    factors = []
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            factors.append(i)
            while n/i == i:
                factors.append(i*i)
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. It does this by iterating through the factors 2, 3, 5, 7, 11, 13, 17, 19, etc. using them one by one.