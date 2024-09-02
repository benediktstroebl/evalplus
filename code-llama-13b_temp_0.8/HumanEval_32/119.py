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
    n = len(xs)
    # 이 조건은 더이상 필요 없다.
    if n % 2 == 1:
        raise ValueError("Function has to be even.")

    # a = xs[0]
    # b = xs[1]
    # c = xs[2]
    # d = xs[3]

    if n == 2:
        return -xs[1] / xs[0]
    elif n == 4:
        a = xs[0]
        b = xs[1]
        c = xs[2]
        d = xs[3]
        return (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a
    else:
        a = xs[0]
        b = xs[1]
        c = xs[2]
        d = xs[3]
        e = xs[4]
        f = xs[5]
        g = xs[6]
        h = xs[7]
        k = xs[8]
        # 임의로 4차 방정식을 작성했다.
        return (-f + math.sqrt(math.pow(f, 2) - 4 * e * d + 4 * e * c * a - 4 * e * b * b + 4 * d * c * b + 16 * d * a * c)) / 2 * e

