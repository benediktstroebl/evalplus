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
    # If the coefficients are all zero, return 0 as the solution
    if all(coeff == 0 for coeff in xs):
        return 0

    # If the coefficients are not all zero and there is an even number of
    # coefficients,
    # we can use Newton's method to find the root.
    if len(xs) % 2 == 0:
        # Newton's method:
        # Given a polynomial f(x) and initial point x0,
        # let's find x1 such that f(x1) = 0 and let's
        # iterate:
        # x_{i+1} = x_i - f(x_i) / f'(x_i)
        # with x_0 = 0.
        # We also know that f(x) has at least one root.
        x0 = 0
        x1 = x0 - poly(xs, x0) / poly(xs[1:], x0)
        x_i = x1

        # The loop stops when we are close enough to the root
        # We stop when (x_{i} - x_{i-1}) / x_{i} < 10 ** -6
        while abs(x_i - x1) / x_i > 10 ** -6:
            x1 = x_i
            x_i = x1 - poly(xs, x1) / poly(xs[1:], x1)

        # return x1
        return x_i

    # If there is an odd number of coefficients,
    # we cannot use Newton's method because the derivative of the
    # polynomial is not defined at x = 0.
    raise ValueError("List should have an even number of coefficients")
