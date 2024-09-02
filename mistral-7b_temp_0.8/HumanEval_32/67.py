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
    x_squared = poly([coeff * 2 for coeff in xs], 2)
    x_cubed = poly([coeff * 3 for coeff in xs], 3)
    x_roots = [x for x in xs if xs[0] * x != 0]

    # test linear functions
    if len(x_roots) == 1:
        x = x_roots[0]
        f = lambda x: poly(xs, x)
        return x

    # test quadratic functions
    elif len(x_roots) == 2:
        root1, root2 = x_roots
        f = lambda x: (root1 - x) * (root2 - x) * poly([coeff for coeff in xs if coeff != 0], 2)
        return find_zero([-x_squared, x_cubed])

    # test cubic functions
    elif len(x_roots) == 3:
        root1, root2, root3 = x_roots
        f =
