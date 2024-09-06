import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Only returns the first solution found.
    Guarantees a solution only if there are an even number of coefficients in xs
    and the largest non-zero coefficient is positive.
    """
    if len(xs) % 2 == 0:
        # In case there are even number of terms,
        # we take greatest coefficient positively
        # to have guaranteed solvability with rational roots
        xs = [max(xs)] if max(xs) > 0 else [abs(max(xs))]
        return _find_zero(xs)
    else:
        return None
def _find_zero(xs):
    """
    Helper function for find_zero.
    """
    x = -xs[0] / (poly(xs, xs[0]))
    return x