

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # if only one term return the derivative as the same polynomial
    if len(xs) == 1:
        return xs[0]

    # if x is not in xs, return zero
    if x not in xs:
        return [0]*len(xs)

    # initialize a list of derivatives
    dxs = [0]*len(xs)

    # loop through each coefficient
    for i, x in enumerate(xs):
        if i == 0:
            dxs[0] += x
        else:
            dxs[i-1] += x*(dxs[i])

    return dxs
