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

    if len(xs) % 2!= 0:
        raise ValueError(f"{len(xs)} coefficients were given, but {len(xs)} coefficients are needed to find the zero point. Please provide even number of coefficients")

    max_non_zero_coeff = max(x for x in xs if x)
    if max_non_zero_coeff == 0:
        raise ValueError(f"Coefficients must not be all zeros. The largest non zero coefficient is {max_non_zero_coeff}")

    x = 0
    if max_non_zero_coeff < 0:
        x = -max_non_zero_coeff
    else:
        x = max_non_zero_coeff

    while poly(xs, x)!= 0:
        x -= 0.001
    return x

