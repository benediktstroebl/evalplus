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

    def find_zeros(xs):
        for i in range(len(xs) - 2):
            if xs[i] == 0:
                continue
            coeff = xs[i]
            power = i + 2
            for j in range(i + 1, len(xs) - 1):
                if xs[j] == 0:
                    continue
                coeff2 = xs[j]
                power2 = j + 2
                if coeff * power2 == coeff2 * power:
                    for k in range(j + 1, len(xs) - 1):
                        if xs[k] == 0:
                            continue
                        coeff3 = xs[k]
                        power3 = k + 2
                        if coeff * power3 == coeff3 * power2:
                            for l in range(k + 1, len(xs) - 1):
                                if xs[l] == 0:
                                    continue
                                coeff4 = xs[l]
                                power4 = l + 2
                                if coeff * power4 == coeff4 * power3:
                                    
