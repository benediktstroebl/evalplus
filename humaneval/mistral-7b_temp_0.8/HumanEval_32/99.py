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
    # if xs is not a list with even number of coefficients
    # and largest non zero coefficient,
    # it means this function is not applicable.
    if len(xs) % 2 != 0 or max([abs(coeff) for coeff in xs]) == 0:
        raise ValueError

    # assume that the polynomial has non zero coefficient of order n
    # in this case we can divide the polynomial by x^n
    # then we obtain a new polynomial in a form of x^n + coeff_n-1 * x^n-1 + ....
    # we can find zero of this polynomial by bisection

    # n is order of the largest non zero coefficient
    n = xs.index(max([abs(coeff) for coeff in xs]))
    # cut off n-1 zeros and multiply coefficient of x^n by -1
    xs = [coeff / (math.factorial(n)) for i, coeff in enumerate(xs)
          if i < n] + [-xs[n]]
    # bisection method
    left = 0
    right
