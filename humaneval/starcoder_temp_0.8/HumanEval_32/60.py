import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # xs must have even number of coefficients.
    if len(xs) % 2!= 0:
        raise ValueError("xs has odd number of coefficients.")
    # find largest coefficient to be used in root finding.
    i = 0
    while xs[i] == 0:
        i += 1
    a = xs[i]
    # find initial root by point division method.
    r = -xs[i - 1] / a
    # get derivative of xs.
    deriv = [i * coeff for i, coeff in enumerate(xs[i - 2::-1])]
    # apply newton's method to find zero point.
    while True:
        f = poly(xs, r)
        # check if root is a zero point.
        if f == 0:
            return r
        # update root
        r = r - f / poly(deriv, r)

