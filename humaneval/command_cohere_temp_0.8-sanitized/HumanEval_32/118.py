import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + ..xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first solution x, even if there are multiple zeros.
    Works only for lists xs with an even number of coefficients,
    and having the largest non-zero coefficient at the end (since we
    are looking for a horizontal asymptote).
    """
    if len(xs) % 2 == 1 or max(xs) == 0:
        return "Invalid input xs"
    xs = list(xs)
    x = 0
    while 1:
        x_prev = x
        x = -xs[0] / xs[-1]
        if abs(x - x_prev) < 1e-6:
            return 'No solution'
        xs[0] *= -1
    while True:
        y = poly(xs, x)
        if y == 0:
            return x
        x += y / xs[-1]