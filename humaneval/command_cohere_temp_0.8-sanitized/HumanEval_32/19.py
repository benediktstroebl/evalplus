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
    Returns only the first found zero solution.
    Works only with lists xs having an even number of coefficients
    and the largest non-zero coefficient.
    """
    # Ensure even number of coefficients and normalize largest coeff to 1
    if len(xs) % 2 == 1:
        xs = [x / abs(x) for x in xs] + [0]
    elif max(xs) == 0:
        xs.append(1)
    # Apply transformation x = y - ((y^2 - n) / (2x)) to shift curve y = 0 to have a zero point at y = n / (2x)
    n = sum(xs) / 2
    ys = [(n - x ** 2) / (2 * x) for x in xs]
    # Find zero of y using binary search
    y_zero = math.sqrt(n)
    left, right = -y_zero, y_zero
    while left < right:
        y_mid = (left + right) / 2
        if poly(ys, y_mid) == 0:
            right = y_mid
        else:
            left = y_mid + 1
    # Finally find x by solving y = n / (2x)
    return (right ** 2 - n) / (2 * right)