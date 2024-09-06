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

    # Check that xs has at least one coefficient
    # and the largest coefficient is non zero
    assert len(xs) >= 1
    assert max(xs) > 0

    # Check that xs has an even number of coefficients
    assert len(xs) % 2 == 0

    # Finds the largest non zero coefficient
    largest_coeff = max([coeff for coeff in xs if coeff > 0])

    # Finds the location of the largest non zero coefficient
    largest_coeff_loc = xs.index(largest_coeff)

    # Finds the first coefficient that has opposite sign of the largest coefficient
    opposite_coeff_loc = 0
    while xs[opposite_coeff_loc] * largest_coeff > 0:
        opposite_coeff_loc += 1

    # Finds the two roots
    x1 = poly(xs[:opposite_coeff_loc], 1) / poly(xs[opposite_coeff_loc], 1)
    x2 = poly(xs[:opposite_coeff_loc], -1) / poly(xs[opposite_coeff_loc], -1)

    # Return the point with smallest absolute value
    if abs(x1) < abs(x2):
        return x1
    else:
        return x2
