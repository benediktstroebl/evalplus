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

    xs = [-x if x > 0 else x for x in xs]

    def binary_search(i, j, eps):
        if j - i <= 1:
            if abs(poly(xs, (i + j) / 2)) < eps:
                return (i + j) / 2
            elif abs(poly(xs, (i + j) / 2)) >= eps:
                if poly(xs, i) * poly(xs, (i + j) / 2) < 0:
                    return binary_search(i, (i + j) / 2, eps)
                else:
                    return binary_search((i + j) / 2, j, eps)
        else:
            if poly(xs, i) * poly(xs, (i + j) / 2) < 0:
                return binary_search(i, (i + j) / 2, eps)
            else:
                return binary_search((i + j) / 2, j, eps)

    return round(binary_search(-1, 1, 0.01), 2)

