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
    assert len(xs) % 2 == 0 and max(xs) != 0
    coeffs = {i: xs[i] for i in range(len(xs))}
    for i in range(1, len(xs) // 2):
        coeffs[i] = xs[len(xs) - i - 1]
        coeffs[-(i + 1)] = xs[i]
    A = [[-coeffs[i] for i in range(len(xs) // 2)]]
    b = [0] * len(xs) // 2
    # A = [[-26, 5, -2], [-6, -2, -2], [-6, 1, -2], [-6, 0, -2], [-6, 2, -2], [-6, 1, 1], [-6, 0, 1], [-6, 2, 1], [-6, 1, 0], [-6, 0, 0]]
    # b = [10, 10, 10, 10, 10, 37, 37, 37, 37, 37]
    for i in range(len(A)):
        for j in range(i):
            A[i].append(A[i - 1][j - 1])
        A[i].append(A[i - 1][-1])
    for i, a in enumerate(A):
        b[i] = round((-coeffs[(len(xs) // 2) - i - 1]) / a[-1], 2)
    # b = [-10.0, -10.0, -10.0, -10.0, -10.0, 19.0, 19.0, 19.0, 19.0, 19.0]
    for i in range(len(A) - 1, -1, -1):
        for j in range(i, len(A)):
            A[i][j] = round(A[i][j] - (A[i][-1] * A[j][-1]), 2)
        b[i] = round(b[i] - (A[i][-1] * b[-1]), 2)
        # x = [(-1, -1, -1, -1