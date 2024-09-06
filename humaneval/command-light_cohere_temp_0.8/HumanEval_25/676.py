```python
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    []
    >>> factorize(55)
    [5, 11]
    >>> factorize(100)
    [2, 2, 33]
    >>> factorize(1000)
    [2, 2, 2, 5, 33]
    """

    if n <= 1:
        return []

    # Create a set to keep track of numbers we've encountered
    # while exploring prime factorization
    factors = set()
    factors_explored = []

    # Use the Euclidean algorithm with iteration to find factors
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.add(i)
            factors_exploured.append(i)

    # Use the set to ensure uniqueness of factors
    factors = list(factors)

    # Sort the factors in descending order of their frequency
    factors.sort(key=lambda x: factors_exploured.count(x))[::-1]

    # Return the list of prime factors in order from smallest to largest
    return factors
```