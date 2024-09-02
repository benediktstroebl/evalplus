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

    def add_roots(x1: float, x2: float):
        x = math.pow((x1 * x2), 1/2)
        return x1 + x2 + x

    max_coeff = max(xs)
    if math.pow(max_coeff, 1/2) % 1!= 0:
        raise Exception('Max coefficient must be a square root of non zero int.')
    if len(xs) % 2 == 1:
        raise Exception('Length of coefficient list must be even.')
    if max_coeff < 0:
        raise Exception('Max coefficient must be non-negative.')
    max_coeff = int(math.pow(max_coeff, 1/2))
    xs.sort(reverse=True)
    n = len(xs)
    # Calculate value of coefficient of each position in polynomial
    ys = [poly([xs[i] for j in range(i)], n) for i in range(max_coeff + 1)]
    roots = set()
    for i in range(len(xs)):
        if
