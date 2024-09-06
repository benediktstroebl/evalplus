

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    length = len(xs)
    derivative_xs = [0] * length

    for i in range(length):
        if i == length - 1:
            derivative_xs[i] = xs[i]
        else:
            derivative_xs[i] = xs[i] * i


    return derivative_xs
