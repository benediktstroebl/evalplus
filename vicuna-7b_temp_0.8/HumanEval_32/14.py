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
        raise ValueError("xs should be a list having an even number of coefficients.")
    if xs[-1] == 0:
        return -math.pi / 2
    coeff_list = [int(coeff) for coeff in xs]
    if len(coeff_list) == 1:
        return round(coeff_list[0], 2)
    else:
        x = list(range(2, len(coeff_list)))
        y = [poly(x, i) for i in range(len(coeff_list))]
        sol = minimize(lambda x: sum([c * x**i for c, i in zip(coeff_list, y)]), 1)
        return round(sol.x, 2)

