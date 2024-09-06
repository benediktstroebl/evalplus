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

    def inner(xs: list, lower: float, upper: float):
        middle = (lower + upper) / 2

        # check if the middle is a solution
        if poly(xs, middle) == 0:
            return middle

        # get lower or upper, where the polynomial is negative
        if poly(xs, lower) * poly(xs, middle) > 0:
            lower = middle
        elif poly(xs, upper) * poly(xs, middle) > 0:
            upper = middle
        else:
            raise Exception(
                "The polynomial has no zero point between lower and upper"
            )

        return inner(xs, lower, upper)

    return inner(xs, -100, 100)

