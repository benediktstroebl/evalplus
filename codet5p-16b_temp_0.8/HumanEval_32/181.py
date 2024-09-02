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

    if len(xs) % 2!= 0:
        raise ValueError("len(xs) must be even")
    if min(xs) * max(xs) > 0:
        raise ValueError("xs must have largest non zero coefficient as first")

    # Calculate number of even coefficients
    n = int(len(xs) / 2)

    # Calculate sum of xs
    sum_xs = sum(xs)

    # Calculate sum of even xs
    sum_even_xs = sum([x for i, x in enumerate(xs) if i % 2 == 0])

    # Calculate sum of odd xs
    sum_odd_xs = sum([x for i, x in enumerate(xs) if i % 2!= 0])

    # Calculate n
    n = int(len(xs) / 2)

    # Calculate left side
    left = sum_odd_xs / n - sum_even_xs

    # Calculate right side
    right = sum_odd_xs / n - sum_xs

    # Calculate quadratic formula
    q = left / right

    
