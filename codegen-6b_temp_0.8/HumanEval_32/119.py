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
    # since all coefficients are positive,
    # non zero coffecients can't be negative
    # so we can first check if we have at least one zero
    # and that there is no negative coefficient
    if xs[0] < 0 or -xs[0] in xs:
        return -1

    # check if x is a zero
    if 0 in xs:
        return xs[0]
    else:
        # next we need to find the index of largest non zero coefficient
        # first compute sign of each coefficient
        signs = [1 if i == 0 else -1 if i < 0 else 1 for i in xs]
        # find the index of non zero coefficient
        idx = xs.index(max(xs))
        if sign(xs[idx]) > 0:
            # now compute (x - 1.)(x - 2.)(x - 3) = -(x - 1) * (x - 2) * (x - 3)
            # since all non zero coffecients are positive,
            # -coeff always positive.
            return -poly(
                [signs[i] * xs[i] for i in range(len(xs))],
                signs[idx] * xs[idx]
            ) / poly(
                [signs[i] * xs[i] for i in range(len(xs))],
                signs[idx - 1] * xs[idx - 1]
            )

        else:
            # now compute (x - 1.)(x - 2.)(x - 3) = -(x - 1) * (x - 2) * (x - 3)
            # since all non zero coffecients are positive,
            # -coeff always positive.
            return -poly(
                [signs[i] * xs[i] for i in range(len(xs))],
                signs[idx - 1] * xs[idx - 1]
            ) / poly(
                [signs[i] * xs[i] for i in range(len(xs))],
                signs[idx] * xs[idx]
            )

