import math
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero solution.
    Works only with lists xs having an even number of coefficients
    and the largest non-zero coefficient.
    """
    assert len(xs) % 2 == 0, "List xs must have an even number of elements"
    x = -xs[0] / (xs[1:] + [0])[0]
    return x