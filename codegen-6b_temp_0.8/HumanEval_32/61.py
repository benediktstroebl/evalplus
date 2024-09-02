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
    # if the polynomial is y = a0x + a1x^1 + a2x^2 + ... x^n, then the roots of a polynomial are the x-coordinates of the
    # intersections of the polynomials (a0x + a1x) and (a2x + a3x^2 + ...) lines, such that the line equations are degree-2.
    # In poly(x), the derivative is expressed as d[k]/dx where k is the ith term of the polynomial.
    # So the line equation is d[k - 1]/ dx = poly[k - 1] / poly[k].
    # The derivative of the polynomial is f(x) = a0 + a1x + a2x^2 + ... + anx^n
    # so the polynomial is of degree n + 1
    n = len(xs) - 1
    # To find a zero, we can try to solve the polynomial given by poly(x) = 0.
    # The following loop to solve polynomial of degree n + 1.
    # The degree of polynomial must be even. If not, we can not find zero.
    for i in range(2, n - 0.5, 2):
        # It is important to check if the coefficients are of the form a0x^n, a1x^n - 1, ...
        # If not, we can not solve the polynomial.
        # E.g. find_zero([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        # is not possible, as it is the very last case.
        # If it is the last case, we must check the last coefficient, as a0 is not of the form a0x^n
        if xs[i] == 0:
            if i == n and xs[-1] != 0:
                raise Exception("This polynomial has no real zero point.")
            # We can not solve the polynomial as all the coeffcients are 0.
            # We skip this case