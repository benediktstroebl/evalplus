

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    i = 0
    new_xs = [0] * len(xs)
    while i < len(xs) - 1:
        new_xs[i] = i * xs[i] + (i + 1) * xs[i + 1]
        i += 1
    return new_xs

