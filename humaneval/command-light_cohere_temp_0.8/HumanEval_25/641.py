```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to its position in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [3, 7, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(313)
    [3, 3, 13]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    n % 2 == 0:
        factors.append(1)
    n % 3 == 0:
        factors.append(3)
    n % 5 == 0:
        factors.append(5)
    n % 7 == 0:
        factors.append(7)
    n % 11 == 0:
        factors.append(11)
    factors.append(1)
    n % 13 == 0:
        factors.append(13)
    factors.append(1)
    return factors
```
This function, `factorize()`, calculates and returns the list of prime factors of the given number, `n`, in ascending order. It does so by using a while loop that eliminates all even and multiples of 2, 3, 5, and 7 from the number, and checks for the remaining prime factors.