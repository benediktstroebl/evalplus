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
    coeffs = [xs[i] for i in range(0, len(xs), 2)]
    # make sure len(coeffs) is odd
    if len(coeffs) % 2 != 1:
        coeffs.append(0)
        # list(coeffs) to get list from generator.
    # iterate over coeffs, popping out the one with min absolute value
    # as we want the smallest non zero coefficient
    coeffs = list(coeffs)
    min_abs_coeff = min(coeffs, key=lambda coeff: abs(coeff))
    coeffs.remove(min_abs_coeff)
    # find the index of the min abs coeff in coeffs
    min_abs_coeff_index = coeffs.index(min_abs_coeff)
    # make sure the min abs coeff is in the last index
    # trick: len(coeffs) is odd, so we add 1, and
    # we have to substract 1 from the index,
    # since we want [-1 + 3] = [-1], and not [-2 + 3] = [-1]
    if min_abs_coeff_index + 1 == len(coeffs):
        coeffs[-1] = -coeffs[-1]
    # get the intersection point
    root = -(min_abs_coeff / (coeffs[-1] + coeffs[min_abs_coeff_index]))
    return root

