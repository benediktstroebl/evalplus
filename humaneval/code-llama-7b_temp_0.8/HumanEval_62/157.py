

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) < 2:
        return []
    # substract first element of the list with second one and append to the final list
    dx = [xs[0]] + [xs[i + 1] * i for i in range(len(xs) - 1)]
    # call the same function recursively
    return dx + derivative(dx)

