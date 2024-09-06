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
        raise ValueError('find_zero only works with even number of coeffcients')
    if len(xs) == 2:
        return -xs[1] / xs[0]
    if len(xs) == 4:
        # If it is a degree 2 polynomial, find_zero can find both zero.
        # However, the solution may be not what we want.
        # This is why I return only one.
        discriminant = math.pow(xs[1], 2) - 4 * xs[0] * xs[2]
        if discriminant < 0:
            return None
        else:
            return (-xs[1] + math.sqrt(discriminant)) / (2 * xs[0])
    # Now, let's think about a degree 4 polynomial.
    # If we have 6 coefficients, the polynomial will be
    # (x - alpha) * (x - beta) * (x - gamma) * (x - delta).
    # However, we don't know if they are all real.
    # So, let's sort them.
    # There will be four of them. Let's call them from small to large
    # alpha, beta, gamma, delta.
    # If they are all real, then beta < gamma < delta.
    # If some of them is imaginary, let's say beta and gamma,
    # then beta < gamma < alpha < delta.
    # So, we can find the zero of the polynomial by finding
    # the intersection of the line y = 0 and the curve
    # (x - alpha) * (x - beta) * (x - gamma) * (x - delta).
    # If beta == gamma, the curve is a straight line,
    # so we can find the zero by setting its derivative zero.
    # If beta < gamma, the curve is a hyperbola,
    # so we can find the zero by setting its discriminant zero.

    # Sorting is O(nlog(n)), but the rest is O(n).
    # So, the complexity is O(nlog(n)).
