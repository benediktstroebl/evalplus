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
    # find largest non zero coefficient
    for i in range(len(xs) - 1, -1, -1):
        if xs[i]!= 0:
            break

    if i == 0:
        # this polynomial has no zeros
        return 0

    def first_derivative(x):
        # polynomial of 1st order
        return i * xs[i] * math.pow(x, i - 1)

    def second_derivative(x):
        # polynomial of 2nd order
        return math.pow(i, 2) * xs[i] * math.pow(x, i - 2)

    # solve equation using Newton's method
    # https://en.wikipedia.org/wiki/Newton%27s_method
    # t = x_{n+1} - x_{n} / f'(x_{n})
    # find x such that x = 0 is a root of f(x) = 0
    # find x such that x' = 0 is a root of f'(x) = 0
    # so x = x' = 0 is a root of f''(x) = 0
    def newton(x):
        return x - (first_derivative(x) / second_derivative(x))

    return newton(0.1)
