```python
def derivative(xs):
    """ xs represent coefficients of a polynomial
        Return derivative of this polynomial in the same form
        >>> xs = [1, 2, 3]
        >>> derivative(xs)
        [2, 6]
        >>> xs = [3, 4, 5]
        >>> derivative(xs) == [6, 10]
        True
        """
    return [float(i) for i in xs[1:-1]]
```