import math
def deriv(xs: list, x: float) -> float:
    """
    Returns derivative of polynomial at point x.
    """
    n = len(xs) // 2
    return sum([(i + 1) * xs[i] * math.pow(x, n - i) for i in range(n)])
def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    zero = 0
    max_val = max(xs)
    while 1:
        x = -zero / max_val
        der = deriv(xs, x)
        if der == 0:
            return x
        prior_zero = zero
        zero = x - der
        if prior_zero == zero:
            raise Exception("Could not find a zero point.")