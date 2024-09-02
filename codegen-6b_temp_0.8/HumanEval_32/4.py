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
    if len(xs) % 2 or (max(xs) == 0 and not min(xs) == 0):
        raise ValueError("argument xs is not valid.")

    def find_zero_inner(xs: list, initial_domain: list):
        """
        inner function for recursive solution.
        generally, inner function use find_zero_inner to solve each subproblem.
        The inner function here is for problem 2.
        """
        for i in range(len(xs)):
            if xs[i] == 0:
                return initial_domain[i]
            if xs[i] != 0:
                t = xs[i]
                xs[i] = 0
                if poly(xs, initial_domain[0]) * t < 0:
                    return find_zero_inner(xs, [initial_domain[0] - t, initial_domain[1]])
                elif poly(xs, initial_domain[0]) * t > 0:
                    return find_zero_inner(xs, [initial_domain[0] + t, initial_domain[1]])
                else:
                    return initial_domain[0]

    return find_zero_inner(xs, [(1 + 10 ** -10) / 2, (1 + 10 ** -10) / 2])

