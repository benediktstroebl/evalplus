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
    n = len(xs)
    assert n % 2 == 0
    max_coeff = max([abs(coeff) for coeff in xs])
    # k is multiplied by 1/2 to make range small enough to make Newton's
    # convergence stable.
    k = int(math.ceil(math.log(max_coeff / 2, 10)))
    # find an x which has the same number of digits as k.
    x = math.pow(10, k)
    # find an x which is in the middle of the range.
    x = x / 2
    while abs(poly(xs, x)) >= 1:
        x -= poly(xs, x) / poly_deriv(xs, x)
    return x

