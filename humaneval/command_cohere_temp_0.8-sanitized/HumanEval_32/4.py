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
    Guarantees a solution only if there are an even number of coefficients,
    and the largest non-zero coefficient is positive.
    """
    if len(xs) % 2 == 0:
        # Ensure largest coefficient is positive for x > 0
        xs = xs[::-1]
    else:
        # Flip the sign of coefficients to find a solution for x < 0
        xs = [-coeff for coeff in xs]

    # Start searching from a very small number (approaching 0)
    # Portion of the below line that is added for the fix:
    x = 1e-5
    while True:
        if poly(xs, x) == 0:
            return x
        # Perform a binary search to find a solution.
        # Portion of the below line that is added for the fix:
        x = (x + 1e-5) / 2