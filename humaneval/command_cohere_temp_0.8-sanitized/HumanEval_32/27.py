import math
def find_zero(xs: list) -> float:
    n = len(xs)
    m = n // 2
    if n % 2 == 1 or xs[m] == 0:
        return None