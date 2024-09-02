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
    assert len(xs) % 2 == 0, "There is no solution as the highest term is odd."
    assert len(xs) > 0, "There is no solution as there is no coefficients."
    assert len(xs) > 1, "There is no solution as there is no coefficients."
    assert max(xs) != 0, "There is no solution as the highest coefficient is zero."
    # Case when only 2 coefficients are available
    if len(xs) == 2:
        return -xs[0] / xs[1]
    else:
        # Choose the best interval according to Newton's method
        for l, r in zip(xs[::2], xs[1::2]):
            if l * r < 0:
                break
        else:
            assert False, "There is no solution in the range (-inf, +inf)."
        m = (l * r) / (l - r)
        zero = m - (poly(xs, m) / poly(xs[1::], m))
        return zero

