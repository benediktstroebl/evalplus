```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [7, 3, 3]
    >>> factorize(55)
    [5, 11]
    >>> factorize(55)
    [5, 5, 11]
    >>> factorize(999)
    [7, 3, 3, 3]
    >>> factorize(3333)
    [3, 3, 3, 1, 1, 1]
    """
    def sieve(limit):
        seen = set()
        for number in range(1, limit+1):
            if number in seen:
                continue
            else:
                seen.add(number)
                for multiple in range(number*number, limit+1, number):
                    if multiple not in seen:
                        seen.add(multiple)
        return seen

    factors = sieve(n)
    return [factor for factor in factors if factor != 0]
```