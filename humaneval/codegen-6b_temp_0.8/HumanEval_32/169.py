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
    # case 1: coefficients are all zero
    if max(xs) == 0:
        return math.inf

    # case 2: coefficients are all positive
    if max(xs) > 0:
        return None

    # case 3: coefficients are all negative
    if min(xs) < 0:
        return None

    # case 4: coefficients are all negative and zero
    if min(xs) == 0 and max(xs) == 0:
        return None

    # else: remove all zero coefficients
    xs = [coeff for coeff in xs if coeff != 0]
    if len(xs) % 2 != 0:
        # if len(xs) % 2 == 1, remove the last coefficeint
        xs.pop()
    n = len(xs)
    # find n/2 points that satisfy the equation
    # xs[:n/2] * xs[n/2:] = 0
    eq_points = []
    for i in range(n // 2):
        if xs[i] * xs[i + n // 2] < 0:
            eq_points.append((xs[i], xs[i + n // 2]))
    if not eq_points:
        return None
    if len(eq_points) == 1:
        return eq_points[0][0] - eq_points[0][1]

    # from eq_points, find a point x such that
    # poly(x) = 0
    a = eq_points[0][0]
    b = eq_points[0][1]
    c = poly(xs, a)
    for i, (x, y) in enumerate(eq_points[1:]):
        if poly(xs, (x + a) / 2) * poly(xs, (x + b) / 2) < 0:
            a = (x + a) / 2
        else:
            b = (x + b) / 2
        c = poly(xs, (a + b) / 2)
    return (a + b) / 2

