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
    # N: length of xs
    N = len(xs)

    # Polynomial
    # Polynomial is xs[0] + xs[1] * x + xs[2] * x^2 + ... xs[N-1] * x^(N - 1)
    # Polynomial is xs[0] + xs[1] * x + xs[2] * x^2 + ... xs[N-1] * x^(N - 1)
    # Find coefficients of polynomial
    # coeff[i] = coeffs[i] * x^(N-i-1)
    # coeff[i] = coeffs[i] * x^(N-i-1)
    # coeffs = [xs[0]]
    # coeffs[1] = xs[0] * x
    # coeffs[2] = xs[0] * x^2
    # coeffs[3] = xs[0] * x^2 * x
    # ...
    # coeffs[N-1] = xs[0] * x^(N-1) * x^(N-1)
    coeffs = [xs[0]]
    for i in range(1, N):
        coeffs.append(xs[i] * math.pow(x, i))

    # Derivative of polynomial is
    # d = sum(coeffs[i] * (i + 1) * x^(i - 1))
    # d = sum(coeffs[i] * i * x^(i - 1))
    # d = sum(coeffs[i] * (i + 1) * (i + 2) * x^(i - 2))
    # ...
    # d = sum(coeffs[i] * i * i * (i + 1) * (i + 2) * x^(i - 3))
    # d = sum(coeffs[i] * (i + 1) * (i + 2) * (i + 3) * x^(i - 4))
    # d = sum(coeffs[i]