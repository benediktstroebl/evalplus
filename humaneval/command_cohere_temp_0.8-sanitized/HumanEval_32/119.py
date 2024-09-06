import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero solution.
    Works only with lists xs having an even number of coefficients
    and the largest non-zero coefficient, as it guarantees
    a solution.
    """
    def find_zero_rec(xs, x):
        """
        Helper function for recursive binary search
        """
        if len(xs) == 1:
            return x == xs[0]
        mid = (xs[0] + xs[1]) / 2.0
        if abs(poly(mid, x)) < 1e-5:  # Floating point precision tolerance
            return True
        elif poly(mid, x) > 0:
            return find_zero_rec(xs[1:], x)
        else:
            return find_zero_rec(xs[:len(xs) - 1], x)

    # Ensure that we have an even number of coefficients and a non-zero largest coefficient
    assert len(xs) % 2 == 0 and xs[-1] != 0

    # Start with a guess close to the largest coefficient
    x = xs[-1] / 2.0
    while True:
        if find_zero_rec(xs, x):
            return x
        x *= 0.5