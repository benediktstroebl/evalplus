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
        raise ValueError("Error: function requires even number of coefficients")

    # get largest coefficient, which is largest in absolute value
    max_coeff = max(abs(coeff) for coeff in xs)

    # convert list to array, so we can use numpy
    xs = list(map(float, xs))
    xs = np.array(xs)

    # initialize new array xs_prime
    xs_prime = xs.copy()
    xs_prime[:] = 0

    # subtract x^i * max_coeff from x^i and add to xs_prime
    for i, x in enumerate(xs):
        xs_prime[i] = x - max_coeff

    # calculate polynomial with coefficient xs_prime
    x = -xs_prime / xs_prime[0]

    return x

