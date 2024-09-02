

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if not isinstance(xs, list):
        raise TypeError("xs should be a list of numbers")
    if len(xs) == 0:
        raise ValueError("xs should have at least one element")
    return [j for i, j in enumerate(xs) if i!= 0] + [0] * (len(xs) - 1)
