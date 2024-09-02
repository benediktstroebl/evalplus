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
    # ls = []
    # for i, coef in enumerate(xs):
    #     if coef == 0:
    #         continue
    #     if coef < 0:
    #         if ls[-1] == -coef:
    #             continue
    #         ls.append(-coef)
    #     else:
    #         ls.append(coef)
    # if not ls:
    #     raise ValueError('Linear system has no solutions')
    # return ls[0] / sum(ls)

    if len(xs) == 1:
        return xs[0]
    if len(xs) % 2 != 0:
        raise ValueError('Polynomial should have even coeffiecients')
    if xs[0] == 0:
        return xs[1] / (-1 * xs[-1])
    if xs[-1] == 0:
        return xs[-2] / (1 * xs[0])
    return sum([coeff * math.pow(-1 * xs[-1], i) for i, coeff in enumerate(xs[1:-1])]) / (xs[0] * xs[-1])

