import math
def find_zero(xs):
    # Check if the list has an even number of coefficients and
    # if it has the largest non-zero coefficient at the end
    if len(xs) % 2 == 0 and xs[-1] == max(xs):
        x = -xs[0] / xs[-1]
        return x
    else:
        return None