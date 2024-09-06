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
    a = len(xs) // 2
    # largest coefficient:
    b = xs[a]

    def is_descending(xs: list):
        return xs[0] > xs[1] and xs[-1] < xs[-2]

    def find_zero_aux(xs: list, lo: float, hi: float):
        """
        helper function of find_zero
        """
        if lo > hi:
            return None

        mid = (lo + hi) / 2
        # find_zero assumes that all points are within range
        # [lo, hi]
        if poly(xs, mid) == 0:
            return mid
        else:
            return find_zero_aux(xs, lo, mid) if poly(xs, lo) * poly(xs, mid) < 0 else find_zero_aux(xs, mid, hi)

    if not is_descending(xs):
        return None
    else:
        return find_zero_aux(xs, -b, b)
