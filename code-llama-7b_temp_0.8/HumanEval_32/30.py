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
    if len(xs) % 2 != 0 or len(xs) == 0:
        raise ValueError("List must have even length")
    if xs[0] != 0:
        raise ValueError("List must not have 0 as its largest coefficient")

    min_x = 0
    max_x = 1
    for i in range(0, len(xs), 2):
        if xs[i + 1] != 0:
            raise ValueError("List must have only 0 in its odd numbered coefficients")
    for i in range(0, len(xs), 2):
        if xs[i] != 0:
            min_x = max_x
            max_x = -min_x * xs[i] / xs[i + 1] + max_x
            break

    def poly_at_mid_x():
        return poly(xs, (min_x + max_x) / 2)

    def newton_step():
        x = poly_at_mid_x()
        dx = (min_x - max_x) / 2
        return poly(xs, x + dx)

    def bisect_step():
        x = (min_x + max_x) / 2
        return poly(xs, x)

    def newton():
        x = newton_step()
        if math.isclose(x, 0):
            return x
        if x > 0:
            min_x = (min_x + x) / 2
        elif x < 0:
            max_x = (max_x + x) / 2
        return newton()

    def bisect():
        x = bisect_step()
        if x > 0:
            min_x = (min_x + x) / 2
        elif x < 0:
            max_x = (max_x + x) / 2
        return bisect()

    try:
        return newton()
    except RecursionError:
        return bisect()
