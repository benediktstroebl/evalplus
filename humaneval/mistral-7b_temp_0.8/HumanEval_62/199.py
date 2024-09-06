

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
        return [0]
    else:
        xs1 = [0] + xs
        xs2 = [0, 0] + xs
        xs3 = [0, 0, 0] + xs

        xs1_xs2_xs3 = (xs1[1] + xs1[2]) * xs2 + (xs2[1] + xs2[2]) * xs3
        return [xs1_xs2_xs3[0]] + xs1_xs2_xs3[1:]
