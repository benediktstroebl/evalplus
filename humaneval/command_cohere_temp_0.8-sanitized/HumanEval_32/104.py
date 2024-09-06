import math
def find_zero(xs: list) -> float:
    n = len(xs)
    if n % 2 == 1 or xs[n // 2] == 0:
        return None
    xs_sorted = sorted(xs)
    return math.sqrt(-xs_sorted[n // 2] / (n // 2))