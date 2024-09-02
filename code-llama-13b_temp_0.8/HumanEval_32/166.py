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
        raise ValueError(
            f"xs has odd number of coefficients. It must be even: {xs}"
        )

    largest_non_zero_coeff = max(xs)
    if largest_non_zero_coeff == 0:
        raise ValueError(
            f"largest_non_zero_coeff must be non zero. It is 0: {xs}"
        )

    # [coeff_1, coeff_2, coeff_3] ~ [coeff_1, coeff_2, coeff_3, 0, 0, 0]
    #
    # Then,
    # find_zero([coeff_1, coeff_2, coeff_3]) = find_zero([coeff_1, coeff_2, coeff_3, 0, 0, 0])
    #                                        = find_zero([coeff_1, coeff_2, coeff_3, 0, 0, 0, 0, 0, 0])
    #
    # find_zero([coeff_1, coeff_2, coeff_3]) = find_zero([coeff_1, coeff_2, coeff_3, 0, 0, 0, 0, 0, 0]) =
    #                                        = find_zero([coeff_1, coeff_2, coeff_3, 0, 0, 0, 0, 0, 0, 0, 0])
    #
    # ...
    #
    # find_zero(xs) = find_zero(xs + [0] * 1000)
    #
    # Thus, we need only even number of coefficients.
    xs += [0] * (1000 - (len(xs) % 2))

    # This is bisection method.
    # https://en.wikipedia.org/wiki/Bisection_method
    l = -1000
    r = 1000
    for _ in range(1000):
        mid = (l + r
