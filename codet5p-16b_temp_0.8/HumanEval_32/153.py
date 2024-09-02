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

    if len(xs) % 2 == 1:
        raise ValueError("list xs has to be even number of coefficients")
    if max(xs) == 0:
        raise ValueError("largest coefficient has to be non zero")
    # find all non zero coefficients
    non_zero_coeffs = []
    for i, coeff in enumerate(xs):
        if coeff!= 0:
            non_zero_coeffs.append(coeff)
    # x_0 ~ x_n are coefficients of x^n
    x_n_coeffs = xs[len(xs) - 1:]
    # x_0 ~ x_(n-1) are coefficients of (x - x_n)
    x_n_minus_1_coeffs = xs[:len(xs) - 1]
    for i in range(len(non_zero_coeffs)):
        xs = x_n_coeffs
        x = non_zero_coeffs[i]
        # calc coefficients of (x - x_n)
        xs.insert(0, -
