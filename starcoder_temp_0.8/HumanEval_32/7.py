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
    # Sort coefficient list to put the highest non zero coefficient to the end.
    xs.sort(reverse=True)
    # Find the highest non zero coefficient.
    highest_coeff = next((i for i, c in enumerate(xs) if c!= 0), len(xs) - 1)
    # Generate the x to be tested.
    x = 1
    while True:
        # Find f(x) = poly(x)
        y = poly(xs[:highest_coeff + 1], x)
        # If f(x) = 0, return x.
        if y == 0:
            return x
        # If f(x) is not 0, update x and continue.
        x += 1
