```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(144)
    [2, 2, 2, 3, 3, 7]
    >>> factorize(session)
    []
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) // + 1,  while n % i == 0:
        factors.append(i)
        n //= i
    for j in factors:
        if j == factors[-1]:
            factors.remove(j)
        else:
            factors.append(j)
    return factors
```
The function factorize returns the list of prime factors of the given number n, in order from the smallest to the largest.  It uses a basic trial and test cases to find the prime factors of a given number.