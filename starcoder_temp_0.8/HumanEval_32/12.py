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
    # find zero point of a polynomial with coefficients xs
    # xs should be a list having even number of coefficients
    # and largest non zero coefficient
    # guaranteed to have a solution
    # if xs is an empty list, raise ValueError
    if xs == []:
        raise ValueError("xs must be a list having even number of coefficients")
    # if xs is not an empty list, then it should be a list having even length
    else:
        # find the index of the largest non zero coefficient
        max_idx = max(range(len(xs)), key=lambda i: xs[i] if xs[i]!= 0 else float("inf"))
        # find x such that poly(x) = 0
        x = (-xs[max_idx]) / xs[max_idx - 1]
        return x
