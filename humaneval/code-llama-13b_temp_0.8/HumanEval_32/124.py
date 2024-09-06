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
    if len(xs) % 2 != 0:
        raise ValueError("xs is expected to have even number of coefficients")
    if xs[0] == 0:
        raise ValueError("xs[0] is expected to be non zero")
    # 1. find range of x so that poly(x) <= 0
    # 2. 1st and 2nd derivative at that range are opposite in sign
    # 3. use newton's method to find x
    a = -100
    b = 100
    while not (poly(xs, a) < 0 and poly(xs, b) > 0):
        a /= 2
        b /= 2
    # newton's method
    x = a
    for _ in range(100):
        x = x - poly(xs, x) / poly_derivative(xs, x)
        if math.isclose(poly(xs, x), 0, rel_tol=1e-6):
            return x

