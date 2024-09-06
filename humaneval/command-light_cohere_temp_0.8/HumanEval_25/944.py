```python
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    for num in range(5, int(n**0.5) // n //= num**2:
        factors.append(num)
        n //= num
    factors.append(int(n))
    return factors
```
The function factorize returns a list of prime factors in order from the smallest to the largest.