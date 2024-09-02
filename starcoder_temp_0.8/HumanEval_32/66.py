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
    assert len(xs) % 2 == 0, "Polynomial degree must be even."
    assert xs[-1]!= 0, "Polynomial coefficients must be non zero."
    # The largest non zero coefficient.
    largest_non_zero_coeff = max(xs)

    # The minimum value of the range.
    a = largest_non_zero_coeff / 2

    # The maximum value of the range.
    b = a + largest_non_zero_coeff

    # The list of all points whose function value is 0.
    zeros = []

    # Iterate over all points.
    while a < b:
        # Evaluate polynomial at the current point.
        val = poly(xs, a)

        # If the function value is 0, record this point.
        if val == 0:
            zeros.append(a)

        # If the function value is positive, shift the range to the right.
        if val > 0:
            a += largest_non_zero_coeff

        # If the function value is negative, shift the range to the left.
        if val < 0:
            b -= largest_non_zero_coeff

    # Return the list of all zero points.
    return zeros
