```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def intersection(s1, s2):
    """
    Determine if the length of the intersection of two closed intervals is prime.
    """
    start = max(s1[0], s2[0])
    end = min(s1[1], s2[1])
    if end >= start:
        length = end - start
        if is_prime(length):
            return "YES"
    return "NO"
```

The `is_prime` function checks if a given number is prime or not. It employs a combination of checks to efficiently rule out multiples of smaller primes. The `intersection` function calculates the intersection of two intervals, and then calls `is_prime` to determine if the length of the intersection is prime.

You can test the function using the following sample inputs/outputs:
```python
>>> intersection((1, 2), (2, 3))
'NO'

>>> intersection((-1, 1), (0, 4))
'NO'

>>> intersection((-3, -1), (-5, 5))
'YES'
```