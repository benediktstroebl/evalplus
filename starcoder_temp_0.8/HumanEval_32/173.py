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
    assert len(xs) % 2 == 0, "xs must be having even number of coefficients."
    largest_coeff = max(xs)
    assert largest_coeff!= 0, "xs must have a largest non zero coefficient."
    # f(x) = (x - largest_coeff) * (x - largest_coeff)...
    # g(x) = -largest_coeff * (x - largest_coeff)...
    x_0 = -largest_coeff

    def f(x):
        return poly(xs, x)
    g = lambda x: -largest_coeff * (x - x_0)

    def find_x_approx(x_0, x_prev):
        x_cur = x_0 - f(x_0) / g(x_0)
        if abs(x_cur - x_prev) < 1e-10:
            return x_cur
        else:
            return find_x_approx(x_cur, x_0)
    return find_x_approx(x_0, x_0 + 10)

