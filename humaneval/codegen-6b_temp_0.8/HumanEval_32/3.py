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
    # assert len(xs) % 2 == 0
    assert all([coff >= 0 for coff in xs])
    A = [xs[i] for i in range(0, len(xs), 2)]
    B = [xs[i] for i in range(1, len(xs), 2)]
    A_norm = [coff for coff in A if coff != 0]
    B_norm = [coff for coff in B if coff != 0]
    if len(A_norm) == 1:
        return -1 * A_norm[0] / B_norm[0]
    elif len(A_norm) == 0:
        return -1 * B_norm[0] / B_norm[1]
    elif len(A_norm) > 1:
        a = A_norm[0]
        b = -1 * B_norm[0] / B_norm[1]
        c = A_norm[1] / B_norm[0]
        # print(a, b, c)
        return (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    else:
        raise Exception("Too many zeros")

