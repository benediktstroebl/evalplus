```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(150)
    []
    >>> factorize(11)
    []
    """

    # method to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**.5)+1):
            if n%i == 0:
            return False
        return True

    # Iterate through each number from 2 to square root of n
    for i in range(2,int(n**.5)+1):
        if is_prime(i):
            for j in range(i*i,n,i):
                if n%j == 0:
                    return [i,j]

    # If no factors found, return an empty list
    return []
```