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
    # if coefficient with maximal absolute value is not largest
    # swap it with largest coefficient
    if abs(xs[0]) < abs(xs[-1]):
        xs = xs[::-1]

    # compute derivative of xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    # return list of [x^0, x^1, x^2,..., x^(n-2)]
    dxs = list(range(len(xs)-1, 1, -1))
    dxs = [c * xs[i+1] for i, c in enumerate(dxs)]
    dxs[0] = xs[0]

    # find roots of derivative xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    # see https://en.wikipedia.org/wiki/Polynomial_root#Factorization
    t = -xs[-1]
    c = dxs[-1]
    for i in range(len(dxs)-2, -1, -1):
        w = c
        c = dxs[i] - t * w
        dxs[i] = w

    # find roots of xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    # x = a0 / a1
    # x^2 + (a1 - a0) * x + a0 = 0
    # x = (-a0 - a1 sqrt(a0^2 - 4 * a1 * a0)) / (2 * a1)
    roots = []
    for i in range(len(dxs)-1, 0, -1):
        a1 = dxs[i]
        a0 = xs[i]
        r = (-a0 - a1 * math.sqrt(a0*a0 - 4 * a1 * a0)) / (2 * a1)
        roots.append(r)
    roots.append(a0 / a1)
    return roots
