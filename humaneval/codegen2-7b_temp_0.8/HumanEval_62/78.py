

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    xs_len = len(xs) - 1
    xs_der = [0] * xs_len
    for i in range(xs_len):
        xs_der[i] = xs[i + 1] + xs_len * xs[i]
    return xs_der
