```python
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(120)
    [2, 2, 2, 3, 5, 7]
    >>> factorize(500)
    [5, 25, 125]
    >>> factorize(3500)
    [7, 5, 3, 35, 3500]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for i in range(int(n**0.5) + 2):
        factors.append(i)
    return factors
```
The function 'factorize' returns a list of prime factors of the given integer 'n' in ascending order. It iterates through loop from smallest to largest prime factors by performing the Euclidean algorithm. The function also checks for the factorization by checking if the number is divisible by any prime number. The function returns the list of prime factors.