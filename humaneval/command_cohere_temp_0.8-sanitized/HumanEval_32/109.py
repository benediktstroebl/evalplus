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
    Returns only the first found zero point.
    Works only with lists xs having an even number of coefficients
    and the largest non-zero coefficient.
    """
    # Ensure xs has even length and the largest non-zero coefficient is last
    if len(xs) % 2 == 1:
        xs.append(0)
    largest_coeff = max(xs)
    if largest_coeff == 0:
        return None
    xs.append(largest_coeff)
    # Sort xs in descending order
    xs = sorted(xs, reverse=True)
    # Initialize guessing range
    l, r = -10, 10
    while l + 1 < r:
        mid = (l + r) // 2
        if poly(xs, mid) == 0:
            r = mid
        else:
            l = mid
    return r