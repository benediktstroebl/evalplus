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
    if len(xs) % 2 == 1:
        raise ValueError('xs must have even number of coefficients')
    xs = xs[:]  # Copy the input list so that the original is not modified
    xs.reverse()
    # Find largest non zero coefficient
    for i in range(len(xs)):
        if xs[i]!= 0:
            largest_non_zero_coeff = xs[i]
            largest_non_zero_coeff_index = i
            break
    largest_non_zero_coeff_index = len(xs) - 1 - largest_non_zero_coeff_index
    if largest_non_zero_coeff_index % 2 == 1:
        raise ValueError('largest non zero coefficient must be a multiple of 2')
    for i in range(largest_non_zero_coeff_index + 1):
        xs[i] /= largest_non_zero_coeff
    for i in range(largest_non_zero_coeff_index, len(xs), 2):
        xs[i] = 0
    return find_zero(xs)

