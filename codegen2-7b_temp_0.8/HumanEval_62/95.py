

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    degree = len(xs) - 1
    xs = np.array(xs)
    if degree == 1:
        return np.array([2 * xs[1]])
    else:
        dxs = derivative(xs[:degree])
        return dxs * np.append(np.array([2]), xs[degree:-1])

