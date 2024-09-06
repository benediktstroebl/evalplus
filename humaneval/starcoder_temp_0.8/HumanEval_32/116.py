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
    # raise error if xs has odd number of elements
    if len(xs) % 2:
        raise ValueError("Coefficients must have even number of elements.")
    # find largest non zero coefficient
    for i in range(len(xs) - 1, 0, -1):
        if xs[i]!= 0:
            break
    # initialize a list for b_i
    bi = [0] * (len(xs) // 2)
    # fill b_i
    for j in range(len(bi)):
        bi[j] = xs[2 * j + 1]
    # initialize a list for a_i
    ai = [0] * (len(xs) // 2)
    # fill a_i
    for j in range(len(ai)):
        ai[j] = xs[2 * j]
    # initialize c_i
    ci = [0] * (len(xs) // 2)
    # fill c_i
    for j in range(len(ci)):
        ci[j] = bi[j] / ai[j]
    # initialize d_i
    di = [0] * (len(xs) // 2 - 1)
    # fill d_i
    for j in range(len(di)):
        di[j] = (bi[j + 1] - ai[j + 1] * ci[j]) / ai[j]
    # find d
    d = (ci[0] + di[0]) / bi[0]
    # find x_0
    x_0 = -d
    for j in range(1, len(ci)):
        x_0 += ci[j] * (math.pow(d, j) - math.pow(d, j - 1)) / (j)
    return x_0

