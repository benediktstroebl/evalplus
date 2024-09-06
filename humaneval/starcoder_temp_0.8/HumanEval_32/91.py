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

    assert len(xs) % 2 == 0, "Non even length list of coefficients"
    assert max(xs[1:])!= 0, "All coefficients are zero!"

    # for the length of the list, it is n + 1
    # when the length of the list is odd, (n + 1) / 2 = n / 2
    # When the length of the list is even, (n + 1) / 2 = (n / 2) + 1
    n = len(xs) // 2 - 1
    xs = xs[::-1]
    a = xs[0]
    b = xs[1]

    for i in range(1, n + 1):
        b = -b
        a, b = b, a + b * xs[2 * i + 1]

    return -b / a
