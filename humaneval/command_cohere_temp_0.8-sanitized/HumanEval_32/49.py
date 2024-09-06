import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    n = len(xs)
    # your code here, make sure it works for n = 2, n = 4, n = 6, n = 8
    if n == 2 and xs[0] != 0:
        return -xs[1] / xs[0]
    elif n % 2 == 1:
        return None
    else:
        # iterate through numbers from -10^6 to 10^6
        for i in range(1, 10**6):
            if poly(xs, i) == 0:
                return i
        return None