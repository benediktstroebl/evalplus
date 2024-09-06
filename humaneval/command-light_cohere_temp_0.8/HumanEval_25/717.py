```python
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    >>> factors = [ [2, 2, 2]
    >>> factors = [5, 5]
    >>> factors = [2, 8, 2, 4, 8, 2]
    >>> factors = [1, 3, 5, 7, 11, 3, 19, 5, 19, 19]
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            for j in range(i, n + 1, i):
                if n / j == i:
                    factors.value.is_ j.
```
 same prime factor.

I hope this solution was helpful! If you require additional assistance or have additional problems you would like me to solve, please do not hesitate to ask.