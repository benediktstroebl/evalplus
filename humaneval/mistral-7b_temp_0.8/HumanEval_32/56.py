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
    if len(xs) % 2 != 0 or xs[len(xs) - 1] == 0:
        return None
    f_of_x = poly(xs, 0.1)
    # 0.1 is only for debugging
    f_of_2 = poly(xs, 2)
    # 2 is only for debugging
    if f_of_x * f_of_2 < 0:
        return None
    x_mid = 1.0
    f_of_x_mid = poly(xs, x_mid)
    while abs(f_of_x_mid) > 0.001:
        if f_of_x_mid == 0:
            return x_mid
        if f_of_x * f_of_x_mid < 0:
            x_mid = (x_mid + 2) / 2
        else:
            x_mid = (x_mid + 1) / 2
        f_of_x_mid = poly(xs, x_mid)
    return
