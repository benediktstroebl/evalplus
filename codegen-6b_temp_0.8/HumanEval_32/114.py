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
    # largest_coefficient = max(abs(coeff) for coeff in xs)
    # for i in range(len(xs)):
    #     if abs(xs[i]) == largest_coefficient:
    #         xs[i] = 0
    #         j = i
    #         while j < len(xs) and xs[j] != 0:
    #             xs[j], xs[j + 1] = xs[j + 1], xs[j]
    #             j += 1
    #         return - j / 2
    # return None

    poly_sum = sum(xs)
    poly_len = len(xs)
    d = poly_sum / poly_len
    if d < 0:
        return None
    elif d == 0:
        return - poly_len / 2
    else:
        for i, coeff in enumerate(xs):
            if coeff != 0:
                break
        else:
            return None
        if (xs[i - 1] == 0) and (xs[i] != 0):
            return - i / 2
        else:
            return - (poly_len - i + (xs[i - 1] != 0)) / 2

