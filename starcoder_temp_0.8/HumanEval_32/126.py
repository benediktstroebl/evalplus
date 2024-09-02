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
    assert (len(xs) % 2 == 0) and (
        xs[0]!= 0
    ), f"xs should be a list of coefficients of a polynomial, xs should have even number of elements and a non zero first element, xs is {xs}"
    start = 0
    end = xs[0]
    while start < end:
        mid = (start + end) / 2
        if poly(xs, mid) == 0:
            return mid
        elif poly(xs, mid) * poly(xs, start) < 0:
            end = mid
        else:
            start = mid
    return mid

