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
    # Your code here
    a, b, c, d = xs[0], xs[1], xs[2], xs[3]

    # assume 2 xs[i] are 0
    # if not, it is impossible to find zero
    # so, your code can't run!

    # substitute into f(x)
    f = a * x**3 + b * x**2 + c * x + d

    # new xs[0] is f(1)
    xs[0] = f(1)

    # new xs[1] is f(2)
    xs[1] = f(2)

    # new xs[2] is f(3)
    xs[2] = f(3)

    # new xs[3] is f(4)
    xs[3] = f(4)

    print(xs)

    # new xs are coefficients of f(x) = a * (x - 1) * (x - 2) * (x - 3
