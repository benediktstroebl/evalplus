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
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number.")
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")
    # Find the roots of the polynomial by solving the quadratic equation
    a = xs[-2]
    b = xs[-3]
    c = xs[-4]
    discriminant = b**2 - 4*a*c
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    if round(poly(xs, root1), 6) == 0:
        return round(root1, 6)
    elif round(poly(xs, root2), 6) == 0:
        return round(root2, 6)
    else:
        raise ValueError("Could not find a root.")
