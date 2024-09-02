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
    # Implement me
    # This function needs to be a recursive function
    # in order to be able to pass tests

    # check if the number of coefficients is even
    if len(xs) % 2 != 0:
        raise Exception("There is not enough coefficients in the polynomial")

    # check if the largest non zero coefficient is a negative number
    largest_non_zero_coefficient = max([abs(coeff) for coeff in xs])
    if largest_non_zero_coefficient < 0:
        raise Exception("Largest non zero coefficient is a negative number")

    # check if the largest non zero coefficient is the first coefficient
    first_coefficient = xs[0]
    if abs(largest_non_zero_coefficient) != abs(first_coefficient):
        raise Exception("Largest non zero coefficient is not the first coefficient")

    # check if there are even number of coefficients
    if len(xs) % 2 == 0:
        midpoint = len(xs) // 2
        # if there are an even number of coefficients
        # divide the coefficients to two polynomials and then
        # find the zero point of each and return the mean of both
        # zero points
        return sum(find_zero(xs[:midpoint])) / midpoint

    # if there are an odd number of coefficients
    # evaluate the polynomial at the midpoint and
    # return the negative or positive value of the
    # midpoint, depending on the sign of the evaluated polynomial
    midpoint = len(xs) // 2
    result = poly(xs, midpoint)
    if result > 0:
        return -midpoint
    elif result < 0:
        return midpoint

