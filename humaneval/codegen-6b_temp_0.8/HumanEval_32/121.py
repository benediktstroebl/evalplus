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
        raise Exception('list xs should have even number of elements')
    if not list(set([c for c in xs if c != 0])):
        raise Exception('list xs should have non zero elements')

    coeff_0 = xs[:1]
    coeff_n = xs[1:]
    for i in range(1, len(xs) // 2):
        coeff_0 += [coeff_n[j] - coeff_n[len(xs) - i - 1] for j in range(i + 1)]
        coeff_n = coeff_0[1:]
    coeff_0 += [coeff_n[j] - coeff_n[len(xs) - i - 1] for j in range(len(xs) - i - 1)]
    coeff_0 += [coeff_0[-1] * -1]
    coeff_0 = coeff_0[:-1]
    return coeff_0[0] / coeff_0[-1]

