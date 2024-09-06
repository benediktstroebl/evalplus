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

    assert len(xs) % 2 == 0
    assert max(xs) > 0
    xs = [coeff for coeff in xs if coeff!= 0]
    xs.sort()
    x0 = 0
    x1 = 1
    if len(xs) == 1:
        return x0
    for x in xs:
        if x == 0:
            return 0
    for i in range(1, len(xs)):
        if xs[i] * xs[i - 1] <= 0:
            x0 = xs[i - 1]
            x1 = xs[i]
            break
    y0 = poly(xs, x0)
    y1 = poly(xs, x1)
    if y0 * y1 > 0:
        raise ValueError("No zero in given polynomial")
    if y0 == 0:
        return x0
    return x1 / (x0 - x1)
