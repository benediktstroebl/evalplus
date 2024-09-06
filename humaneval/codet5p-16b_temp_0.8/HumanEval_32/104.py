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

    max_non_zero = -math.inf
    max_non_zero_index = 0
    for i, coeff in enumerate(xs):
        if coeff!= 0 and coeff > max_non_zero:
            max_non_zero = coeff
            max_non_zero_index = i
    if max_non_zero_index % 2!= 0:
        return None
    xs = xs[max_non_zero_index:]
    xs.reverse()
    zero = xs[0]
    for i in range(len(xs) - 1):
        zero += xs[i] * math.pow(-1, i + 1)
    return zero / max_non_zero
    
    
