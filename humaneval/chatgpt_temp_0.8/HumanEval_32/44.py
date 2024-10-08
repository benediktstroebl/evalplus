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
        raise ValueError("xs must have even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("largest non-zero coefficient required")
    # Using the Rational Root Theorem to find possible roots
    possible_roots = [i / xs[-1] for i in range(1, abs(xs[-1])+1)]
    possible_roots += [-i / xs[-1] for i in range(1, abs(xs[-1])+1)]
    # Checking which root is the actual solution
    for root in possible_roots:
        if abs(poly(xs, root)) < 1e-10:
            return root
    raise ValueError("solution not found")
