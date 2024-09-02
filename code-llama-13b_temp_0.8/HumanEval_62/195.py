

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The naive implementation of the derivative is to multiply each coefficient
    #  by its degree. However, we can take advantage of the fact that the
    #  derivative of a sum is the sum of the derivatives, so we can get away
    #  with a lot less work.
    # The derivative of a constant is 0, so we don't need to handle that case.
    if len(xs) == 1:
        return []
    else:
        return [degree * coefficient for coefficient, degree in zip(xs[1:], range(1, len(xs)))]

    #  less efficient solution:
    # if len(xs) == 1:
    #     return []
    # else:
    #     return [coefficient * degree for coefficient, degree in zip(xs, range(1, len(xs) + 1))]
