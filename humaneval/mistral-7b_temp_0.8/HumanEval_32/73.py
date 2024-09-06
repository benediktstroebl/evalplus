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
    # ensure xs have only even number of coefficients
    if len(xs) % 2 == 1:
        xs.append(0)

    # find the largest non zero coefficient
    max_abs_coeff = max(abs(coeff) for coeff in xs)
    max_index = xs.index(max_abs_coeff)

    # find sign of largest coefficient
    sign = 1 if max_abs_coeff > 0 else -1

    # use the largest coeffient to find the value of
    # 1/max_coeff * poly(x) = f(1/max_coeff * x)
    poly_func = lambda x: poly(xs, x) / max_abs_coeff
    poly_func = lambda x: poly_func(x) * sign
    return 0 if poly_func(0) == 0 else poly_func(0) / poly_func(1)

