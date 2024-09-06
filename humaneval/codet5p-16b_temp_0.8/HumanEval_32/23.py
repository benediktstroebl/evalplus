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

    assert len(xs) % 2 == 0, "List xs must have even number of coefficients."
    assert max(xs)!= 0, "All coefficients must be non zero."
    xs = xs + xs[-1:]  # make list xs as symmetric

    max_idx = len(xs) // 2
    max_coeff = max(xs)
    max_degree = len(xs) - xs.index(max_coeff) - 1
    assert max_degree > 1, "List xs must have at least two non zero coefficients."
    max_divide = max_coeff / max_degree
    max_quo, max_rem = divmod(max_coeff, max_degree)
    assert max_rem == 0, "Largest coefficient must be a multiple of the highest degree."
    assert max_divide == max_quo, "The largest coefficient must be a multiple of the highest degree."

    def find_zero_of_poly(x: float):
        return poly(xs, x)

    x = max_divide
    for i in range
