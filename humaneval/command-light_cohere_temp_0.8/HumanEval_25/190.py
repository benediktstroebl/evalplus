```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(77)
    [3, 3, 7]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 7]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int(n))
    return factors
```
This function factorizes the given number into a list of prime factors in the order of decreasing magnitude. It uses the fundamental method to factorize numbers. The time complexity of the function is O(log n), as it only iterates up to the square root of the number being factorized.