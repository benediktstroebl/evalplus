import math
def find_zero(xs: list) -> float:
    n = len(xs)
    if n % 2 == 1 or xs[n // 2] == 0:
        return "Coefficients list should have even length and the largest non-zero coefficient to guarantee exactly one zero point.";

    # bottom half => negative reciprocals of coefficients
    b = [(-1) / x for x in xs[:n // 2]]
    # top half => positive reciprocals of coefficients
    t = [1 / x for x in xs[n // 2:]]

    m = len(b) - 1
    x_upper_bound = 10**10
    x_lower_bound = -10**10
    for i in range(m):
        while x_upper_bound - b[i] <= 1e-6:
            x_upper_bound += b[i]
        while x_lower_bound - b[i] <= 1e-6:
            x_lower_bound -= b[i]

    for i in range(m, 0, -1):
        while t[i - 1] + b[i] <= 1e-6:
            x_upper_bound /= t[i - 1]
        while t[i - 1] - b[i] <= 1e-6:
            x_lower_bound /= t[i - 1]

    return x_lower_bound + 0.5 * (x_upper_bound - x_lower_bound)