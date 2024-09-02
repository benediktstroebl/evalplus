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

    # sanity check
    if len(xs) % 2 == 0:
        # take only non zero coefficients
        nonzero_coefficients = [coeff for coeff in xs if coeff!= 0]
        # get largest coefficient
        largest_coefficient = max(nonzero_coefficients)
        # construct new list of coefficients in order to make find_zero function as O(log n)
        new_xs = [coeff / largest_coefficient for coeff in xs]
        # find zero point using bisection method
        left = 0
        right = largest_coefficient
        # if poly is even then zero point must be in [a, b], if poly is odd then zero point must be in (a, b]
        if poly(xs, left) * poly(xs, right) < 0:
            return bisection_method(new_xs, left, right)
        else:
            return bisection_method(new_xs, left, right + 0.000001)
    else:
        raise Exception(
            "find_zero function takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution"
        )

