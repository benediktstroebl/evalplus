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

    assert len(xs) % 2 == 0, "only even number of coefficients is allowed"
    assert max(xs) > 0, "largest non zero coefficient is allowed"

    xs = [abs(coeff) for coeff in xs]
    xs = sorted(xs, reverse=True)
    xs = [coeff / math.factorial(i) for i, coeff in enumerate(xs)]
    xs = [coeff if coeff > 0 else -coeff for coeff in xs]
    xs = [coeff for coeff in xs if coeff!= 0]
    xs = sorted(xs, reverse=True)

    zero_pt = poly(xs, 0)
    zero_pt = -zero_pt if zero_pt < 0 else zero_pt
    zero_pt = zero_pt / (xs[0] * xs[1]) if len(xs) > 1 else -zero_pt
    zero_pt = zero_pt / math.factorial(len(xs) - 1) if len(xs) > 2 else zero_pt

    return zero_pt
