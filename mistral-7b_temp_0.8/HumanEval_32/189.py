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
    # TODO: implement this function
    # Example: f(x) = x^2 + 3x + 4
    #  f'(x) = 2x + 3
    # f'(x) = 0 when x = -3/2
    # f(-3/2) = -3/2 * (-3/2) + 3 * (-3/2) + 4 = 1/2
    # so -3/2 is zero point for f(x)
    if len(xs) % 2 == 0:
        coeff = xs[-1]
        coeff_neg = xs[-2]
        x = (-coeff + math.sqrt(math.pow(coeff, 2) - math.pow(coeff_neg, 2))) / coeff_neg
        return x
    return None

