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
    assert n % 2 == 0, "xs must have even number of coefficients"
    largest_non_zero_coeff = max(xs[1::2])
    assert largest_non_zero_coeff!= 0, "largest non zero coefficient is zero"
    # xs are coefficients of a polynomial.
    xs = [coeff / largest_non_zero_coeff for coeff in xs]
    xs = [x for x in xs if x!= 0]
    if n == 2:
        return -xs[1] / 2 + math.sqrt(xs[1] ** 2 / 4 + xs[0]) / 2
    delta = poly(xs, 1)
    if delta > 0:
        print(f"This is not a quadratic equation. delta = {delta}")
        return None
    return poly(xs, 0) / 2 + math.sqrt(poly(xs, 1) / 2)
