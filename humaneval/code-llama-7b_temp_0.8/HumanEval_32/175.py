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
    # xs must have even number of coefficients
    assert len(xs) % 2 == 0

    # largest non-zero coefficient is exist.
    # Otherwise, there is no solution.
    max_index = 1
    for i in range(2, len(xs)):
        if xs[i] != 0:
            max_index = i
            break

    x = 0
    while True:
        # divide coefficient by largest non-zero coefficient
        # for example,
        # xs = [2, -2, 1, 0] => [1, -1, 0]
        # x = 0 => 1 * x^0 - 1 * x^1 + 0 * x^2 = 1
        # x = 1 => -1 * x^0 + 0 * x^1 = -1
        # x = 2 => 0 * x^0 = 0
        quotient = poly(xs[:max_index], x) / xs[max_index]
        if quotient == 0:
            return x
        x += quotient

