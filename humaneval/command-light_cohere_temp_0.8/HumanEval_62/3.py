```python
def derivative(xs: list):
    """
   xs represent coefficients of a polynomial
    Returns the derivative of this polynomial in the same form
    >>> derivative([3, 1, 2])
    [6, 2]
    >>> derivative([3, 1, 2, 3])
    [6, 6]
    """
    n = len(xs)
    result = [0] * n
    for i in range(1, n):
        result[i] = xs[i - 1] + xs[i] * xs[i - 2]
    return result
```