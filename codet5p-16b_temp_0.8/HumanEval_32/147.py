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

    coefficients = list(xs)
    is_poly_zero = True
    is_poly_positive = True
    is_poly_negative = True
    while len(coefficients) >= 2:
        # Calculate polynomial value and check if it is equal to zero
        poly_val = poly(coefficients, coefficients[-1])
        if round(poly_val, 2) == 0:
            return round(coefficients[-1], 2)
        # Find degree of polynomial
        degree = len(coefficients)
        # Calculate derivative of polynomial
        derivative = []
        for i, coeff in enumerate(coefficients):
            derivative.append(degree * coeff - i * coeff)
        # Sort coefficients of polynomial by decreasing order
        derivative.sort(reverse=True)
        # If polynomial is positive, then there is a root in interval [0, x]
        if derivative[0] > 0:
            is_poly_zero = False
            is_poly_positive = False
        # If polynomial is negative
