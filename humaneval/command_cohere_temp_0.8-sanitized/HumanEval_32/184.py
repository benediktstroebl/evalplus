import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + .. xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes lists xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # check if xs has even length andLargest coefficient is not zero
    if len(xs) % 2 == 0 and xs[-1] != 0:
        # let k be largest index
        k = len(xs) // 2
        # swap coefficients xs[0] and xs[k]
        xs[0], xs[k] = xs[k], xs[0]
        # return sum of (xs[0] * x**i - xs[k] * x**(i+k)
        return poly([0, xs[0]], 0) - poly([0, xs[k]], 0) / xs[k]
    else:
        return "bad_input"