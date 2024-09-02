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
    if len(xs) % 2 != 0 or any([coeff for coeff in xs if coeff != 0]):
        raise ValueError("find_zero only takes list xs of even number of coefficients. "
                         "list xs with non zero coefficent do not work.")

    def is_poly_zero(xs: list, x: float):
        return poly(xs, x) == 0

    def has_bounded_roots(xs: list):
        return len(set(xs)) <= 1

    def is_useless(xs: list, i):
        return xs[i] * xs[i + 1] == 0

    def is_useless_after_one_root(xs: list):
        return len(xs) - len(set(xs)) <= 1

    #  we can only have a single root;
    #  if there are more, it is easy to get infinite polynomial.
    for i in range(len(xs)):
        if is_poly_zero(xs, i / 2) and not is_useless(xs, i):
            if is_useless_after_one_root(xs[i + 1:]):
                ret = 1 / 2 * (i / 2 + 1)
                if ret == int(ret):
                    return ret
    raise ValueError("poly does not have zero root")

