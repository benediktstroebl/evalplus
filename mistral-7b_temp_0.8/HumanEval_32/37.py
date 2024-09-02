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
    # Find largest coefficient.
    # Find index of largest coefficient.
    # Iterate through all coefficients and accumulate partial sum.
    # After summing a coefficient, if sum > 0, subtract
    # the value of largest coefficient.
    # If sum < 0, add value of largest coefficient.
    #
    # 1. Find largest coefficient
    coefficients = [coeff for coeff in xs]
    largest_coefficient = max(abs(coeff) for coeff in coefficients)
    #print("Largest coefficient: ", largest_coefficient)

    # 2. Find index of largest coefficient
    idx_largest_coefficient = max(
        enumerate(coeffs), key=lambda idx: abs(idx[1])
    )[0]
    #print("Index of largest coefficient: ", idx_largest_coefficient)

    # 3. Iterate through all coefficients and accumulate partial sum
    partial_sum = 0
    idx = idx_largest_coefficient
    while idx >= 0:
        partial_sum += coefficients[idx]
        #
