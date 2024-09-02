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
        raise ValueError("Polynomial must be even degree")

    # x_bar is the average of zero coefficient and leading coefficient
    x_bar = (0 - xs[0]) / 2

    # zero point is either
    # 1. smaller than x_bar
    # 2. larger than x_bar
    # 3. (x_bar - x_bar) which is 0
    for i in range(len(xs)):
        # largest non-zero coefficient is 1
        if xs[-i] == 1:
            return x_bar - (math.sqrt(x_bar * x_bar - 4 * xs[-1 - i]) / 2)
        # smallest non-zero coefficient is -1
        elif xs[i] == -1:
            return x_bar + (math.sqrt(x_bar * x_bar - 4 * xs[i + 1]) / 2)

    # if there are only two coefficients and neither of them are 1 or -1
    if len(xs) == 2:
        return -xs[1] / xs[0]

    return 0
