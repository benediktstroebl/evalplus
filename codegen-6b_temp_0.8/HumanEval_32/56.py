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
    xs.sort()

    # no zero found
    if xs[0] > 0:
        return -1

    # must be even
    if len(xs) % 2 != 0:
        return -1

    # must have non zero coefficient
    if xs[0] == 0:
        return -1

    # find number of coefficients
    n = len(xs)

    # find max pos of coefficient
    max_pos = -1
    for i in range(n):
        if xs[i] > 0 and max_pos < i:
            max_pos = i

    # power of max_pos
    power = math.log(max_pos, 2)

    if power - int(power) != 0.0:
        return -1.0

    power = int(power)

    # find positive and negative roots
    roots = []
    if xs[0] < 0:
        power_root = math.pow(-xs[0], 1.0 / power)
        roots.append(-power_root)
        roots.append(power_root)
    else:
        power_root = math.pow(xs[0], 1.0 / power)
        roots.append(power_root)
        roots.append(-power_root)

    # find zeros
    # x^y = -1 = <- root
    for i in range(1, power):
        if power_root * xs[i] != -1.0:
            roots.append(-1.0 / power_root)

    return roots

