import math
def find_zero(xs: list) -> float:
    n = len(xs)
    m = n // 2
    if n % 2 == 1 or xs[m] == 0:
        return None
    xs[0], xs[m] = xs[m], xs[0]
    x = (xs[m]**2 - xs[1]) / (24 * xs[m] + xs[m]**2)
    return x