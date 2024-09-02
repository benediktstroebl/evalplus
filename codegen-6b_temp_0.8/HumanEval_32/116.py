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
    # Identify x = -((coeffs[n] - coeffs[0]) / coeffs[1])
    # Find extreme case if coefficients are all equal
    if abs(xs[1]) < 1e-6:
        return -xs[0] / xs[2]
    a = [1, 1]
    for i in range(1, len(xs)):
        a.append((xs[i] - xs[0]) / xs[1])
    b = [1]
    for i in range(1, len(xs)):
        b.append(i * (xs[i] - xs[0]) / xs[1])
    c = [xs[0]]
    for i in range(1, len(xs)):
        c.append(xs[0] + xs[1] * i)
    # Solve the linear system
    try:
        x = -(a[2] * b[1] - b[2] * a[1]) / (a[2] * b[0] - b[2] * a[0])
        y = b[2] - a[2] * (x * a[0] + b[0]) / a[2]
    except ZeroDivisionError:
        return None
    return (x, y)

